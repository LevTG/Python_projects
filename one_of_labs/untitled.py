import turtle
turtle.shape ('turtle')
turtle.speed(2)

def draw(l,n):
	if n == 0:
		turtle.forward(l)
		return
	else:
		n -= 1
		draw(l/3,n)
		turtle.left(60)
		draw(l/3,n)
		turtle.right(120)
		draw(l/3,n)
		turtle.left(60)
		draw(l/3,n)
draw(30,2)