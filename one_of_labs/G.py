def get_M(n):
	M = []
	for i in range(n):
		A = list(map(int, input().split()))
		M.append(A)
	return M

def IsSymetric(A):
	for i in range(n):
		for k in range(n):
			if A[i][k] != A[k][i]:
				return False
	else:
		return True

n = int(input())
M = get_M(n)
if IsSymetric(M):
	print('YES')
else:
	print('NO')