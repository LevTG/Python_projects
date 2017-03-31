def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1

def sort(A):
	for i in range(len(A)):
		tmp = A[i]
		k = i - 1
		
		for i in range(len(A)):
			if k < 0 or A[k] < tmp:
				break
			A[k + 1] = A[k]
			k -= 1
		A[k + 1] = tmp


get_next.seed = int(input())
freq = {}
thing = get_next()

while thing != 0:
	if thing not in freq:
		freq[thing] = 1
	else:
		freq[thing] += 1
	thing = get_next()

val = list(freq.values())
key = list(freq.keys())

maxm = max(val)

i = 0
Max = []
for i in range(len(val)): 
	if val[i] == maxm:
		Max.append(key[i])
sort(Max)
print(*Max)


