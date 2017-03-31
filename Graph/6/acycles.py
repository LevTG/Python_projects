import networkx as nx

def read_graph():
	graph = nx.DiGraph()
	n, m = [int(x) for x in input().split()]
	for i in range(m):
		a, b = [int(x) for x in input().split()]
		graph.add_edge(a, b)
	return graph, n, m

graph, n, m = read_graph()
if nx.is_directed_acyclic_graph(graph):
	print("YES")
else:
	path = nx.find_cycle(graph, orientation = 'original')
	for edge in path:
		print(edge[0], end = ' ')
