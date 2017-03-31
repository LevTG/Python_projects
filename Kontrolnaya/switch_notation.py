def sw(A, base):
	if len(A) == 1:
		if int(A) / base == 0:
			return '0'
		else:
			return str(A%base) + str(A//base)

	return str(int(list(A).pop() % base)) + sw(list(int(A) // base), base) 

S = input().split()
n = int(S[0])
A = S[1]
k = int(S[2])

int(A, n)
list(A)

print(sw(A, k))