def get():
	S = list(map(int, input().split()))
	x = S[0]
	y = S[1]
	return x, y

i = 0
x, y = -1, -1

while (x, y) != (0, 0):
	if x%3 == 0 and y%3 != 0 and y%2 == 0:
		i += 1
	elif x%3 != 0 and y%3 == 0 and x%2 == 0:
		i += 1
	elif x % 9 == 0 and y % 9 == 0:
		i += 1
	x, y = get()
print(i) 
