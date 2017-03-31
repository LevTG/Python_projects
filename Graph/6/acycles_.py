def read_graph():
	N, M = [int(x) for x in input().split()]
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
	return graph, N, M

def get_cycle(that, graph, used, path = None):
	used[that] = 1
	if path == None:
		path = []
	path.append(that)

	for other in graph[that]:
		if used[other] == 0:
			if(get_cycle(other, graph, used, path)[0]):
				return True, path
			else:
				path.pop()
		elif used[other] == 1:
			path.append(other)
			return True, path
	used[that] = 2
	return False, path

graph, n, m = read_graph()

used = {}
for i in range(len(graph)):
	used[i] = 0

for i in range(len(graph)):
	if used[i] != 2:
		is_cycle, path = get_cycle(i, graph, used)
		if is_cycle:
			break
else:
	print("YES")
	exit(0)

v = path.pop()
print(' '.join(map(str, path[path.index(v):])))