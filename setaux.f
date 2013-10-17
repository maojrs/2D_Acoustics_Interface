c     ============================================
      subroutine setaux(mbc,mx,my,xlower,ylower,dx,dy,
     &                  maux,aux)
c     ============================================
c
c     # set auxiliary arrays 
c     # dummy routine when no auxiliary arrays
c
c     
      implicit double precision (a-h,o-z)
      dimension aux(maux,1-mbc:mx+mbc,1-mbc:my+mbc)

      common /cparam/ rho,bulk,rho2,bulk2,rho3,bulk3
      common /cparam/ cc,zz,cc2,zz2,cc3,zz3

      do i=1-mbc,mx + mbc
        indexi = i !+ mbc
        xcell = xlower + (indexi-0.5d0)*dx
        do j=1-mbc,my + mbc
          indexj = j! + mbc
          ycell = ylower + (indexj-0.5d0)*dy
          if (abs(xcell) .le. 0.007 .and. abs(ycell) .le. 0.007) then
            aux(1,i,j) = zz3
            aux(2,i,j) = cc3
          else
            aux(1,i,j) = zz
            aux(2,i,j) = cc
          end if
          if (abs(xcell) .le. 0.006 .and. abs(ycell) .le. 0.006) then
            aux(1,i,j) = zz2
            aux(2,i,j) = cc2
          end if	    
!           print*,i,j, zz,cc,zz2,cc2
        end do
       end do
c
       return
       end
