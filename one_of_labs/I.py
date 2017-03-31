
def get_M(n):
	M = []
	for i in range(n):
		A = list(map(int, input().split()))
		M.append(A)
	print('\n')
	return M

def PRINT(A):
    for i in range(len(A)):
        print(' '.join(map(str, A[i])))
    print('\n')

def move_line(A, i, st, uord):
	if st:
		if uord:
			for k in range(i, len(A) - i - 1):
				A[k][i] = A[k + 1][i]
		else:
			for k in range(len(A) - i - 1, i, -1):
				A[k][i] = A[k - 1][i]
	elif uord:
		for k in range(len(A) - i - 1, i, -1):
			A[i][k] = A[i][k - 1]
	else:
		for k in range(i, len(A) - i - 1):
			A[i][k] = A[i][k + 1]

def chng_crl(A, i):
	for k in range(len(A) - i - 1):
		p = A[i][i]
		move_line(A, i, 1, 1)
		PRINT(A)
		move_line(A, len(A) - i - 1, 0, 0)
		PRINT(A)
		move_line(A, len(A) - i - 1, 1, 0)
		PRINT(A)
		move_line(A, i, 0, 1)
		A[i][i + 1] = p
		

def Rotate(A):
	i = 1
	while i != n // 2:
		chng_crl(A, i)
		PRINT(A)
		i += 1

n = int(input())
M = get_M(n)
Rotate(M)
PRINT(M)