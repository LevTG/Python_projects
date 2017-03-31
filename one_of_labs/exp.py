def PRINT(A, n):
    for i in range(n):
        print(' '.join(map(str, A[i])))


n = int(input())
A = [['.'] * n for i in range(n)]
for k in range(n):
    A[k][k] = '*'
    A[k][- k - 1] = '*'
    mid = n // 2
    A[k][mid] = A[mid][k] = '*'

#if - k - mid > - n:
 #   A[k][- k - mid - 1] = '*'
  #  A[- k - mid - 1][- k - 1] = '*'
#
#if k + mid < n:
 #   A[- k - 1][k + mid] = '*'
  #  A[k + mid][k] = '*'
PRINT(A, n)



