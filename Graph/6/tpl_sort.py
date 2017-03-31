def read_graph():
	N, M = [int(x) for x in input().split()]
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
	return graph, N, M

"""
def tpl_sort(that, graph, used, checked, k):
	used.add(that)
	checked.append(that)
	for other in graph[that][1]:
		if other in checked:
			print('NO')
			exit(0)
		if other not in used:
			k = tpl_sort(other, graph, used, checked, k)
	graph[that] = k, graph[that][1]
	checked.pop()
	return k + 1
"""

def tpl_sort(that, graph, used, checked, path):
	used.add(that)
	checked.append(that)
	for other in graph[that]:
		if other in checked:
			print('NO')
			exit(0)
		if other not in used:
			path = tpl_sort(other, graph, used, checked, path)
	path.append(that)
	checked.pop()
	return path

graph, n, m = read_graph()
checked = []
used = set()
path = []

for i in range(n):
	if i not in used:
		path = tpl_sort(i, graph, used, checked, path)
print(" ".join(map(str, path[::-1])))