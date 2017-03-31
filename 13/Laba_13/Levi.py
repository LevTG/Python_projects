import turtle as ttl

def Levi(n, x = 4000):
	if n < 0 or x < 0:
		return "Error! Wrong value!"

	if n == 0:
		ttl.forward(x)
		return

	l = x/2

	ttl.left(45)
	Levi(n - 1, l)
	ttl.right(90)
	Levi(n - 1, l)
	ttl.left(45)

Levi(int(input()), int(input()))
input()
