A = int(input()) 
l = [] 
while A >= 17: 
	l.append(A % 17) 
	A = A//17 
	

l.append(A) 
n = 0 
for i in range(len(l)): 
	if l[i] == 16: 
		n+=1 
print(n)