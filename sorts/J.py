def qsort(A, l, r):
	i = 0
	last = 0
	if l > r:
		return
	A[l], A[(l + r)//2] = A[(l + r)//2], A[l]
	last = l
	for i in range(l + 1, r + 1):
		if len(A[i]) < len(A[l]):
			last += 1
			A[last], A[i] = A[i], A[last]
	A[l], A[last] = A[last], A[l]
	qsort(A, l, last - 1)
	qsort(A, last + 1, r)

N = int(input())
A = []
for i in range(N):
	A.append(input())
qsort(A, 0, N - 1)
print(A)




def input_dict(a, dicts): 
	b = len(a) 
	value = dicts.get(b, []) 
	value = value + [a[::-1]+' ' + a] 
	dicts[b] = value 
	return dict 

dicts = {} 
b = [] 
n = int(input()) 

for i in range(n): 
	input_dict(input(), dicts) 

sp = dicts.keys() 
sp = sorted(sp) 

for key in sp: 
	b = sorted(dicts[key]) 
	print(key, *b, sep='\n') 




















