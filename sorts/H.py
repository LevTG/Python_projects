def compare(a1, b1):
	a = a1
	b = b1
	max = 0
	if a%10 < b%10:
		return 1
	elif a%10 == b%10:
		return compare(a//10, b//10) 	
	else:
		return 2


N = int(input())
A = list(map(int, input().split()))
B = []
mini = 89898
for p in range(N):
	for k in A:
		i = compare(k, mini)
		if i == 1:
			mini = k
		if i == 2:
			continue
	B.append(mini)
	A.pop(A.index(mini))
	mini = 99999
print(' '.join(map(str, B)))


