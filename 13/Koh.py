import turtle as ttl

def Koh(n, x = 300):
	if n < 0 or x < 0:
		return "Error! Wrong value!"

	if n == 0:
		ttl.forward(x)
		return

	l = x/3
	Koh(n - 1, l)
	ttl.left(60)
	Koh(n - 1, l)
	ttl.right(120)
	Koh(n - 1, l)
	ttl.left(60)
	Koh(n - 1, l)

Koh(3)
input()