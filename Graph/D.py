def read_graph():
	N, M = [int(x) for x in input().split()]
	graph = [(None, []) for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a][1].append(b)
		graph[b][1].append(a)
	return graph, N, M

def skat(that, graph, used, path, k = 0):
	graph[that] = k % 2, graph[that][1]
	if graph[that][0] == 0:
		path.append(that)
	used.add(that)
	for other in graph[that][1]:
		if other in used and graph[that][0] == graph[other][0]:
			print('NO')
			exit(0)
		if other not in used:
			path = skat(other, graph, used, path, k + 1)
	return path

graph, n, m = read_graph()
path = []
used = set()
for i in range(n):
	if i not in used:
		path = skat(i, graph, used, path)
print(' '.join(map(str, path)))