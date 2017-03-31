def sort(A, B):
	for k in range(len(A)):
		for i in range(len(A) - k - 1):
			if A[i] > A[i + 1]:
				A[i], A[i + 1] = A[i + 1], A[i]
				B[A[i]] += 1
				B[A[i + 1]] += 1
		
def prinT(A, B):
	C = []
	for i in range(len(A)):
		C.append(str(A[i]) + ':' + str(B[A[i]]))
	print(*C)

A = list(map(int, input().split()))
Num = [0] * len(A)
Books = dict(zip(A, Num))
sort(A, Books)
prinT(A, Books)