S = list(input())
B = []
n = 0
for i in S:
	if i == '(':
		B.append(0)
		n += 1
	elif i == ')':
		if len(B) == 0:
			n = -1
			break
		B.pop()
		n -= 1
if n > 0 or n == -1:
	print("NO")
else:
	print("YES")