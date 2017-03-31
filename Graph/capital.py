def read_graph():
	N, M = [int(x) for x in input().split()]
	graph = {i:{} for i in range(N)}
	for j in range(M):
		a, b, c = [int(x) for x in input().split()]
		graph[a][b] = c
		graph[b][a] = c
	return graph, N, M

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

graph, n, m = read_graph()
min_l = float('+inf')
curr = 0
for v in graph.keys():
	dist = dijkstra(graph, v)
	s = sum(list(dist.values()))
	if s < min_l:
		min_l = s
		curr = v
print(curr)