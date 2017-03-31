import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

	#   добавляем рёбра и вершины

G.add_edge('a', 'b', weight=0.6)
G.add_edge('a', 'c', weight=0.2)
G.add_edge('c', 'd', weight=0.1)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.3)

elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]  # "тяжёлые"
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5] # "лёгкие"

pos = nx.spring_layout(G) # позиции всех вершин

	# вершины
nx.draw_networkx_nodes(G, pos, node_size=700)

	# рёбра
nx.draw_networkx_edges(G, pos, edgelist=elarge,
					width=6)                                   # "тяжёлые"
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='b', style = 'dashed') # "лёгкие"

	# метки
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # сохранить как png картинку
plt.show() # вывести на экран