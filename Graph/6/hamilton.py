def read_graph():
	N, M = [int(x) for x in input().split()]
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
		graph[b].append(a)
	return graph, N, M

def is_hamilton(graph, path):
	for i in range(len(graph) - 1):
		if path[i + 1] not in graph[i]:
			return False
	if path[len(graph) - 1] not in graph[0]:
		return False
	return True

graph, n, m = read_graph()
for i in range(