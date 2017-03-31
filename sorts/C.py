n = int(input())
A = list(map(int, input().split()))
def buble(A, k):
	s = int(100000 / (10 ** k))
	for t in range(1, len(A)):
		for i in range(0, len(A) - t):
			if A[i]%s > A[i+1]%s:
				A[i], A[i+1] = A[i+1], A[i]
	return A
for i in range(1, 6):
	A = buble(A, i)
print(*A)