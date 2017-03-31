def qsort(A, B, l, r):
	i = 0
	last = 0
	begin = 0
	if l > r:
		return
	A[l], A[(l + r)//2] = A[(l + r)//2], A[l]
	B[l], B[(l + r)//2] = B[(l + r)//2], B[l]
	last = l
	for i in range(l + 1, r + 1):
		if A[i] < A[l]:
			last += 1
			A[last], A[i] = A[i], A[last]
			B[last], B[i] = B[i], B[last]
		elif A[i] == A[l]:
			last += 1
			qsort(B, A, l, last)
	A[l], A[last] = A[last], A[l]
	B[l], B[last] = B[last], B[l]
	qsort(A, B, l, last - 1)
	qsort(A, B, last + 1, r)

def NULLs(a1, rasm):
	a = a1
	a *= rasm
	i = 0
	while a % 10 == 0 and a // 10 != a1:
		a //= 10
		i += 1
	if int(a) == a1:
		a = str(a1) + '0' * (i - 1)
	else:
		a = str(a1) + '0'*i
	return a

def Print(A, B):
	for i in range(len(A)):
		print(NULLs(B[i], 100), NULLs(A[i], 1000))


n = int(input())
L = []
W = []
for i in range(n):
	C = list(map(float, input().split()))
	L.append(C[0])
	W.append(C[1])
qsort(W, L, 0, n - 1)
Print(W, L)
