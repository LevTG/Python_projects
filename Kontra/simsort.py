def sort(A, B):
	for k in range(len(A)):
		for i in range(len(A) - k - 1):
			if A[i] >= A[i + 1]:
				A[i], A[i + 1] = A[i + 1], A[i]
				B[i], B[i + 1] = B[i + 1], B[i]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort(A, B)
print(*B)