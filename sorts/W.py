n = int(input())
A = list(truple(map(float, input().split())) for i in range(n))
for j in range(1, len(A)):
	for i in range(len(A) - j):
		if A[i][1] == A[i + 1][1] and A[i][0] < A[i + 1][0]:
			A[i], A[i + 1] = A[i + 1], A[i]
for k in range(n):
	print("%.2f" %A[k][0], "%.3f" %A[k][1])