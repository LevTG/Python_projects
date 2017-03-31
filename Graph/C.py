import heapq as hq
def read_graph():
	line = list(map(int, input().split()))
	n, m = line[0], line[1]
	graph = {i:{} for i in range(n)}
	for i in range(m):
		a, b, w = [int(x) for x in input().split()]
		graph[a][b] = w
		graph[b][a] = w
	return n, m, graph, line[2:]

def dijkstra(graph, start, n, d):
	d[start][start] = 0
	used = set()
	Q = [(0, start)]
	while Q:
		d_c, curr = hq.heappop(Q)
		if d_c != d[start][curr]:
			continue
		for near in graph[curr]:
			l = d[start][curr] + graph[curr][near]
			if l < d[start][near]:
				d[start][near] = l
				hq.heappush(Q, (l, near))
		used.add(curr)
	return d

n, m, graph, major = read_graph()
low = {vert: {vert: float('+inf') for vert in graph} for vert in graph}
for i in range(n):
	low = dijkstra(graph, i, n, low)
okrugs = [None] * n

for i in range(n):
	lower = float('+inf')
	for capital in major:
		if lower > low[i][capital]:
			lower = low[i][capital]
			okrugs[i] = capital
	if okrugs[i] == None:
		okrugs[i] = -1
print('\n'.join(map(str, okrugs)))