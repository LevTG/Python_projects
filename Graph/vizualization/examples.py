import matplotlib.pyplot as plt
import networkx as nx

G = nx.path_graph(8)
nx.draw(G)
plt.savefig("simple_path.png")
plt.show() 




#***************************************************************



import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G) # позиции всех вершин

# вершины
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0,1,2,3], # список вершин
                       node_color='r',     # красный цвет
                       node_size=500,      # размер
                       alpha=0.8)          # прозрачность

nx.draw_networkx_nodes(G, pos,
                       nodelist=[4,5,6,7],
                       node_color='b',
                       node_size=500,
                       alpha=0.8)

# рёбра
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5) # все рёбра
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0,1),(1,2),(2,3),(3,0)],
                       width=8, alpha=0.5, edge_color='r')   # красные рёбра
nx.draw_networkx_edges(G, pos,
                       edgelist=[(4,5),(5,6),(6,7),(7,4)],
                       width=8, alpha=0.5, edge_color='b')   # синие рёбра

# добавим математические названия вершин
labels={}
labels[0]=r'$a$'
labels[1]=r'$b$'
labels[2]=r'$c$'
labels[3]=r'$d$'
labels[4]=r'$\alpha$'
labels[5]=r'$\beta$'
labels[6]=r'$\gamma$'
labels[7]=r'$\delta$'
nx.draw_networkx_labels(G, pos, labels, font_size=16)

plt.axis('off')
plt.savefig("labels_and_colors.png") # сохранить как png картинку
plt.show() # вывести на экран
