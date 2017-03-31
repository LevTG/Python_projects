def read_graph():
	N = int(input())
	graph = [[] for i in range(N)]
	for j in range(N):
		graph[j] = list(map(int, input().split()))
	print()
	return graph, N

Matrix, N = read_graph()
for i in range(N):
	for j in range(N):
		if Matrix[i][j] == 0:
			continue
		print(i, j, Matrix[i][j])
