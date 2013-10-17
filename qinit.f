
c
c
c
c     =====================================================
       subroutine qinit(meqn,mbc,mx,my,xlower,ylower,
     &                   dx,dy,q,maux,aux)
c     =====================================================
c
c     # Set initial conditions for q.
c     # Acoustics with smooth radially symmetric profile to test accuracy
c
       implicit double precision (a-h,o-z)
       dimension q(meqn, 1-mbc:mx+mbc, 1-mbc:my+mbc)
       
      common /cparam/ rho,bulk,rho2,bulk2,rho3,bulk3
      common /cparam/ cc,zz,cc2,zz2,cc3,zz3
c
      pi = 4.d0*datan(1.d0)
      width = 0.002

      do i=1,mx
            xcell = xlower + (i-0.5d0)*dx
            do j=1,my
              ycell = ylower + (j-0.5d0)*dy
          pressure = 101325.0 + 82737.0 ! +dexp(-5000000.0*(xcell-(xlower + 0.001))**2)
          u = 380.d0
              if (xcell .ge. -0.0085) then
                pressure = 101325.0
                u = 0.d0
              end if
              q(1,i,j) = pressure
              q(2,i,j) = u !0.d0
              q(3,i,j) = 0.d0
            end do
       end do
       return
       end
