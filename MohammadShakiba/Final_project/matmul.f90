subroutine ADD(a, b, c)
   implicit none
   real, intent(in) :: a, b
   real, intent(out) :: c
   c = a + b
end subroutine ADD

subroutine matmul(A, B, C, N)
    implicit none
    integer, intent(in) :: N
    real, intent(in) :: A(N,N), B(N,N)
    real, intent(out) :: C(N,N)
    integer :: i, j, k
    
    do i = 1, N
        do j = 1, N
            C(i,j) = 0.0
            do k = 1, N
                C(i,j) = C(i,j) + A(i,k) * B(k,j)
            end do
        end do
    end do
end subroutine matmul
