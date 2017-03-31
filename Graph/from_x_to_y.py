def read_graph():
	N, M, x, y = [int(x) for x in input().split()]
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
		graph[b].append(a)
	return graph, N, M, x, y

def dfs(graph, start, used = None):
	time = {start: 0}
	if used == None:
		used = set()
	used.add(start)
	Q = [start]
	while Q:
		curr = Q.pop(0)
		for near in graph[curr]:
			if near not in used:
				used.add(near)
				Q.append(near)
				time[near] = time[curr] + 1
	return time
graph, n, m, x, y = read_graph()
time = dfs(graph, x)
print(time[y])