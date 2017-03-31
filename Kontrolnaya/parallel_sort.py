def hoar_sort(A, B):
	if len(A) <= 1:
		return A
	
	barrier = random.choice(A)
	L_a, M_a, R_a = [], [], []
	L_b, M_b, R_b = [], [], []

	for i in range(len(A)):
		if A[i] < barrier:
			L_a.append(A[i])
			L_b.append(B[i])

		elif A[i] == barrier:
			M_a.append(A[i])
			M_b.append(B[i])

		else:
			R_a.append(A[i])
			R_b.append(B[i])

	return hoar_sort(L_a, L_b) + hoar_sort(M_a, M_b) + hoar_sort(R_a, R_b)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
hoar_sort(A, B)
print(A, B)
