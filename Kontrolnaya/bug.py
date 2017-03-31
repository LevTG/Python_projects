def bug(n):
	K = [0, 1] + [None] * (n + 1)
	for i in range(2, n + 1):
		K[i] = K[i - 1] + K[i - 2]
	return K[n]

print(bug(4))