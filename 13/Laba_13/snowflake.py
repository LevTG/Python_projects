import turtle as ttl

def Koh(n, x = 300):
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
	

def snowflake(n):
	if n < 0:
		return
	for i in range(3):
		Koh(n)
		ttl.right(120)

n = int(input())
snowflake(n)
input()