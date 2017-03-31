import matplotlib.pyplot as plt
import networkx as nx

def read_graph():
	graph = nx.Graph()
	line = input()
	labels = {}
	while line:
		a, b, c = [x for x in line.split()]
		c = int(c)
		graph.add_edge(a, b, weight = c)
		if a not in labels:
			labels[a] = a
		if b not in labels:
			labels[b] = b
		line = input()
	return graph, labels

def draw_graph(graph, labels, pos):
	nx.draw_networkx_labels(graph, pos, labels, font_size = 5)
	nx.draw_networkx_edges(graph, pos)
	nx.draw_networkx_nodes(graph, pos, node_size = 500, node_color = 'y')

	plt.axis('off')
	plt.savefig('graph_1.png')
	plt.show()

def base(graph, start, labels, pos):
	used = set()
	used.add(start)
	Q = [start]
	while Q:
		curr = Q.pop(0)
		for near in graph[curr]:
			if near not in used:
				used.add(near)
				Q.append(near)
				graph[curr][near]['edge_color'] = 'red'
				print(graph[curr][near])
	draw_graph(graph, labels, pos)

def base_2(that, graph, checked = set()):
	checked.add(that)
	for other in graph[that]:
		if other not in checked:
			Base.add_edge(that, other, weight = graph[that][other]['weight'])
			base_2(other, graph, Base, checked)
	return Base


graph, labels = read_graph()
pos = nx.spring_layout(graph)
draw_graph(graph, labels, pos)
base(graph, graph.nodes()[0], labels, pos)
#Base = base_2(graph.nodes()[0], graph)
#draw_graph(Base, labels, pos)

#D_1
Is_E = nx.is_eulerian(graph)
print("This graph is Eulerian:", Is_E)
if Is_E:
	Eulerian = nx.eulerian_circuit(graph)
	print(Eulerian)
	nx.draw_networkx_edges(graph, pos, edgelist = Eulerian, edge_color = 'r', width = 5)
	plt.show()

