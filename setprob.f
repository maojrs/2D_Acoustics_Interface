      subroutine setprob
      implicit double precision (a-h,o-z)
      character*25 fname
      common /cparam/ rho,bulk,rho2,bulk2,rho3,bulk3
      common /cparam/ cc,zz,cc2,zz2,cc3,zz3

c
c     # Set the material parameters for the acoustic equations
c
c
      iunit = 7
      fname = 'setprob.data'
c     # open the unit with new routine from Clawpack 4.4 to skip over
c     # comment lines starting with #:
      call opendatafile(iunit, fname)
                
c
c     # Density and bulk modulus:

      read(7,*) rho
      read(7,*) bulk
      read(7,*) rho2
      read(7,*) bulk2
      read(7,*) rho3
      read(7,*) bulk3
c
c     # Compute sound speed and impendance:

      cc = dsqrt(bulk/rho)
      zz = rho*cc
      cc2 = dsqrt(bulk2/rho2)
      zz2 = rho2*cc2
      cc3 = dsqrt(bulk3/rho3)
      zz3 = rho3*cc3

      return
      end
