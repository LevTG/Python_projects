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

def Print(keys, vals):
	for i in range(len(keys)):
		print("%c: %d", keys[i], vals[i], end = '\t')

freq = dict()
line = input()
for char in line:
	if char not in freq:
		freq[char] = 1
	else:
		freq[char] += 1

keys = list(freq.keys())
vals = list(freq.values())
qsort(vals, keys, 0, len(keys) - 1)

Print(keys, vals)