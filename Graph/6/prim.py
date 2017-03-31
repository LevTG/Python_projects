def read_graph():
	n, m = [int(x) for x in input().split()]
	graph = {i:{} for i in range(n)}
	for i in range(m):
		a, b, c = [int(x) for x in input().split()]
		graph[a][b] = c
		graph[b][a] = c
	return graph, n, m

def Prim(graph, start, n):
	INF = 10**9
	dist = [INF] * n
	dist[start] = 0
	used = [False] * n
	used[start] = True
	tree = []
	tree_w = 0
	for i in range(n):
		min_d = INF
		for j in range(n):
			if not used[j] and dist[j] < min_d:
				min_d = dist[j]
				p = j
		tree.append((i, p))
		tree_w += graph[i][p]
		used[p] = True
		for v in range(n):
			dist[v] = min(dist[v], graph[p][v])
	return tree, tree_w

graph, n, m = read_graph()
tree, w = Prim(graph, 0, n)
print(tree, w)