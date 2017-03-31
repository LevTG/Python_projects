import turtle as ttl

def Dragon(n, x = 100000, sign = 1):
	if n < 0 or x < 0:
		return "Error! Wrong value!"

	if n == 1:
		ttl.forward(x)
		return

	ttl.left(45 * sign)
	Dragon(n - 1, x / 2, 1)
	ttl.right(90 * sign)
	Dragon(n - 1, x / 2, -1)
	ttl.left(45 * sign)

Dragon(18)
input()
