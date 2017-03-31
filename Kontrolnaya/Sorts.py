def hoar_sort(A):
	if len(A) <= 1:
		return A
	barrier = random.choice(A)
	L, M, R = [], [], []

	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	return hoar_sort(L) + hoar_sort(M) + hoar_sort(R)

def merge(L, R):
	A = [None] * (len(L) + len(R))
	i = j = k = 0
	while i < len(L) and j < len(R):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1
	A[k:] = L[i:] + R[j:]
	return A

def merge_sort(A):
	if len(A) <= 1:
		return A
	L = merge_sort(A[:len(A)//2])
	R = merge_sort(A[len(A)//2:])

	return merge(L, R)

A = list(input().split())
hoar_sort(A)
print(A)