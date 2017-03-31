import turtle as ttl

def Mink(n, x = 400):
	if n < 0 or x < 0:
		return "Error! Wrong value!"

	if n == 0:
		ttl.forward(x)
		return

	l = x/8
	Mink(n - 1, l)
	ttl.left(90)
	Mink(n - 1, l)
	ttl.right(90)
	Mink(n - 1, l)
	ttl.right(90)
	Mink(n - 1, l)
	Mink(n - 1, l)
	ttl.left(90)
	Mink(n - 1, l)
	ttl.left(90)
	Mink(n - 1, l)
	ttl.right(90)
	Mink(n - 1, l)


Mink(2)
input()