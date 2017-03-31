def qsort(A, l, r):
	i = 0
	last = 0
	if l > r:
		return
	A[l], A[(l + r)//2] = A[(l + r)//2], A[l]
	last = l
	for i in range(l + 1, r + 1):
		if A[i] < A[l]:
			last += 1
			A[last], A[i] = A[i], A[last]
	A[l], A[last] = A[last], A[l]
	qsort(A, l, last - 1)
	qsort(A, last + 1, r)

A = list(input())
qsort(A, 0, A.index('.') - 1)
print(''.join(A[0:A.index('.') + 1]))
