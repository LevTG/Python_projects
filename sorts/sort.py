def redix_sort(A):
	max_len = len(str(max(A)))
	for i in range(max_len):
		B = [[] for i in range(10)]
		for x in A:
			digit = (x//10**i)%10
			B[digit].append(x)
			
		A[:] = []
		for k in range(10):
			A.extend(B[k])
		print(A, B)
	return A

A = [1, 5, 6, 110, 232, 22, 33, 9000]
print(redix_sort(A))

