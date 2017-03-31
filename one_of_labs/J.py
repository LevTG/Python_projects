def get_M(n):
	M = []
	for i in range(n):
		A = list(map(int, input().split()))
		M.append(A)
	return M

def PRINT(A, n):
    for i in range(n):
        print(' '.join(map(str, A[i])))

def look_around(F, i, j):
	for k in i - 1, i, i + 1:
		for l in j -1, j, j + 1:
			if k < 0 or l < 0 or k >= len(F) or l >= len(F[0]):
				continue

			if F[k][l] != '*':
				F[k][l] += 1


A = list(map(int, input().split()))
N = A[0]
M = A[1]
K = A[2]
Mines = get_M(K)
Field = [[0] * M for i in range(N)]
for i in range(K):
	Field[Mines[i][0] - 1][Mines[i][1] - 1] = '*'
for i in range(K):
	look_around(Field, Mines[i][0] - 1, Mines[i][1] - 1)
PRINT(Field, N)