def get():
	S = list(map(int, input().split()))
	x = S[0]
	y = S[1]
	return x, y



def gener(N, K, prefix = ''):
	if n == 1:
		 
	else:
		gener(N - 1, K - 1, prefix = '1')
		gener(N - 1, K, prefix = '0')


N, K = get()

gener(N, K)
