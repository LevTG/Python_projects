def read_graph():
	n = int(input())
	graph = [[] for i in range(n)]
	for i in range(n):
		line = list(map(int, input().split()))
		for j in range(n):
			if line[j] != 0:
				graph[i].append(j)
	return graph, n

graph, n = read_graph()
input()
colors = list(map(int, input().split()))
numb = 0

for that in range(n):
	for near in graph[that]:
		if colors[that] != colors[near]:
			numb += 1
print(numb // 2)