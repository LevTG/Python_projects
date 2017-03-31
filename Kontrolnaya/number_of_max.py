A = list(map(int, input().split()))

while A[-1] != 0:
	A.pop()

print(A.count(max(A)))