def get_M(n):
	M = []
	for i in range(n):
		A = list(map(int, input().split()))
		M.append(A)
	return M

def PRINT(A, n):
    for i in range(n):
        print(' '.join(map(str, A[i])))

A = list(map(int, input().split()))
n = A[0]
m = A[1]

M = get_M(n)

B = list(map(int, input().split()))
i = B[0]
j = B[1]

for k in range(n):
	M[k][i], M[k][j] = M[k][j], M[k][i]

PRINT(M, n)