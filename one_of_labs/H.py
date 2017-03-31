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
Mt = [[0] * n for i in range(m)]
M = get_M(n)
for i in range(n):
	for k in range(m):
		Mt[k][i] = M[i][k]
PRINT(Mt, m)