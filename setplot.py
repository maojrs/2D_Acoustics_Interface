
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

import os
if os.path.exists('./1drad/_output'):
    qref_dir = os.path.abspath('./1drad/_output')
else:
    qref_dir = None
    print "Directory ./1drad/_output not found"


#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from clawpack.visclaw import colormaps

    plotdata.clearfigures()  # clear any old figures,axes,items data
    

    # Figure for pressure
    # -------------------

    plotfigure = plotdata.new_plotfigure(name='Pressure', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [-0.01, 0.01]
    plotaxes.ylimits = [-0.01, 0.01]
    plotaxes.title = 'Pressure'
    plotaxes.scaled = True      # so aspect ratio is 1

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = 0
    plotitem.pcolor_cmap = colormaps.yellow_red_blue
    plotitem.pcolor_cmin = 90000 #0.8
    plotitem.pcolor_cmax = 350000 #2.2
    plotitem.add_colorbar = False
    
    #plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    #plotitem.contour_nlevels = 10
    #plotitem.contour_colors = 'k'
    #plotitem.contour_min = 0.8
    #plotitem.contour_max = 2.2
    #plotitem.show = True  

    
    # Plot outline of interface
    def aa(current_data):
      from pylab import linspace,plot
      #gcs = 2.0/200.0
      x = [-0.007,-0.007,0.006,0.006,-0.006,-0.006,0.006,0.006,-0.007]
      y = [0.007,-0.007,-0.007,-0.006,-0.006,0.006,0.006,0.007,0.007]
      # Draws the cap
      x2 = [0.006, 0.007,0.007,0.006,0.006]
      y2 = [-0.007,-0.007,0.007,0.007,-0.007]
      # Draw the transwell
      x3 = [0.006,0.003,-0.003] 
      y3 = [0.006,0.002,0.002]
      x4 = [-0.003,0.003,0.006]
      y4 = [-0.002,-0.002,-0.006]
      x5 = [-0.003,-0.003]
      y5 = [0.002,-0.002]
      #y[:] = [xx - gcs for xx in y]
      plot(x,y,'k',linewidth=2.0)
      plot(x2,y2,'k',linewidth=2.0)
      plot(x3,y3,'--k', linewidth=1.0)
      plot(x4,y4,'--k', linewidth=1.0)
      plot(x5,y5,'--r',linewidth=4.0)
      
    plotaxes.afteraxes = aa
    

    # Figure for scatter plot
    # -----------------------

    plotfigure = plotdata.new_plotfigure(name='scatter', figno=3)
    plotfigure.show = (qref_dir is not None)  # don't plot if 1d solution is missing

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0,1.5]
    plotaxes.ylimits = [-2.,4.]
    plotaxes.title = 'Scatter plot'

    # Set up for item on these axes: scatter of 2d data
    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    
    def p_vs_r(current_data):
        # Return radius of each grid cell and p value in the cell
        from pylab import sqrt
        x = current_data.x
        y = current_data.y
        r = sqrt(x**2 + y**2)
        q = current_data.q
        p = q[0,:,:]
        return r,p

    plotitem.map_2d_to_1d = p_vs_r
    plotitem.plot_var = 0
    plotitem.plotstyle = 'o'
    plotitem.color = 'b'
    plotitem.show = (qref_dir is not None)       # show on plot?
    
    # Set up for item on these axes: 1d reference solution
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = qref_dir
    plotitem.plot_var = 0
    plotitem.plotstyle = '-'
    plotitem.color = 'r'
    plotitem.kwargs = {'linewidth': 2}
    plotitem.show = True       # show on plot?
    plotaxes.afteraxes = "pylab.legend(('2d data', '1d reference solution'))"
    

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
