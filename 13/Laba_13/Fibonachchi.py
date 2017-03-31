def Fib(n, f0 = 0, f1 = 1):
	if n < 0:
		return "ERROR! Wrong value"
	if n == 0:
		return f0
	else:
		return Fib(n - 1, f1, f0 + f1)

n = int(input())
print(Fib(n))

