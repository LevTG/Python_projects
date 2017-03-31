def get_next(): 
	get_next.seed = (get_next.seed*513 + 1)%2**18
	if get_next.seed == 0:
		return 0
	else:
		return (get_next.seed**2%100000 + 1) 
get_next.seed = int(input()) 





max_ = 0
Max = []
thing = get_next()
i = 0

while thing != 0:
	if thing > max_:
		max_ = thing
		Max = [i]
	
	elif thing == max_:
		Max.append(i)
	
	thing = get_next()
	i += 1

print(*Max)