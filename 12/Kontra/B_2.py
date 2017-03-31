def mark(graph, i):
	a = i % 8
	b = (i - 6) % 8
	c = (i - 10) % 8
	d = (i - 17) % 8
	e = (i - 15) % 8
	f = (i + 6) % 8
	j = (i + 10) % 8
	h = (i + 15) % 8
	k = (i + 17) % 8
	if i + 10 <= 63 and i + 10 >= 0 and abs(a-j)<=2:
		graph[i].append(i + 10)
	if i + 6 <= 63 and i + 6 >= 0 and abs(a-f)<=2:
		graph[i].append(i + 6)
	if i + 17 <= 63 and i + 17 >= 0 and abs(a-k)<=2:
		graph[i].append(i + 17)
	if i + 15 <= 63 and i + 15 >= 0 and abs(a-h)<=2:
		graph[i].append(i + 15)
	if i - 15 <= 63 and i - 15 >= 0 and abs(a-e)<=2:
		graph[i].append(i - 15)
	if i - 17 <= 63 and i - 17 >= 0 and abs(a-d)<=2:
		graph[i].append(i - 17)
	if i - 10 <= 63 and i - 10 >= 0 and abs(a-c)<=2:
		graph[i].append(i - 10)
	if i - 6 <= 63 and i - 6 >= 0 and abs(a-b)<=2:
		graph[i].append(i - 6)

def str_to_number(name):
	return d[name[0]] + 8 * (int(name[1]) - 1)

def numb_to_str(numb):
	a = numb % 8
	c = (numb - a) // 8 + 1
	s = n[a]
	g = str(c)
	return s + g

def bfs(graph, start, finish, used = None):
	path = [[] for i in range(len(graph))]
	if used is None:
		used = set()

	used.add(start)
	Q = [start]
	while Q:
		that = Q.pop(0)
		for n in graph[that]:
			if n not in used:
				used.add(n)
				Q.append(n)
				path[n] += path[that]
				path[n].append(that)
			if n == finish:
				return path[finish] + [finish]


dask = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
n = {dask[letter]: letter for letter in dask}

start  = str_to_numb(input())
finish = str_to_numb(input())

graph = [[] for i in range(64)]
for i in range(64):
	mark(graph, i)

path = bfs(graph, start, finish)
for i in path:
	print(numb_to_str(i))