def read_graph():
	N, M, x, y = [int(x) for x in input().split()]
	graph = {i:{} for i in range(N)}
	for j in range(M):
		a, b, c = [int(x) for x in input().split()]
		graph[a][b] = c
		graph[b][a] = c
	return graph, N, M, x, y

def dijkstra(graph, start):
	dist = {v: float('+inf') for v in graph}
	dist[start] = 0
	used = set()
	while len(used) != len(graph):
		min_d = float('+inf')
		for v in dist:
			if dist[v] < min_d and v not in used:
				curr = v
				min_d = dist[v]
		used.add(curr)
		for near in graph[curr]:
			l = dist[curr] + graph[curr][near]
			if l < dist[near]:
				dist[near] = l
		used.add(curr)
	return dist

graph, n, m, x, y = read_graph()
dist = dijkstra(graph, x)
print(dist[y])