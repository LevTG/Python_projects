def read_graph():
	n = int(input())
	graph = [[]*n for i in range(n)]
	for i in range(n):
		line = list(map(int, input().split()))
		for j in range(n):
			if line[j] != 0:
				graph[i].append(j)
	return graph, n

graph, n = read_graph()
k = input()
k = 0
colors = list(map(int, input().split()))

for that in range(n):
	for near in graph[that]:
		if colors[that] != colors[near]:
			k += 1
print(k // 2)