def chet(m):
	B = [0] * m
	for i in range(0, m, 2):
		B[i] = '*'
	for i in range(1, m, 2):
		B[i] = '.'
	return B[:]

def nechet(m):
	B = [0] * m
	for i in range(0, m, 2):
		B[i] = '.'
	for i in range(1, m, 2):
		B[i] = '*'
	return B[:]

def PRINT(A, n):
    for i in range(n):
        print(' '.join(map(str, A[i])))

A = list(map(int, input().split()))
n = A[0]
m = A[1]
Ch = chet(m)
NCh = nechet(m)
Otvet = []

for i in range(n):
	if i % 2 == 0:
		Otvet.append(NCh)
	else:
		Otvet.append(Ch)
PRINT(Otvet, n)
