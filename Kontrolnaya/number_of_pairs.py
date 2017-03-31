def check(x, y):
	if x % 2 == 0 and y % 7 == 0 and (x > 99 or y > 99):
		return True
	else:
		return False


A = list(map(int, input().split()))
x = A[0]
y = A[1]
i = 0

while x != 0 or y != 0:
	if check(x, y):
		i += 1
	A = list(map(int, input().split()))
	x = A[0]
	y = A[1]


print(i)