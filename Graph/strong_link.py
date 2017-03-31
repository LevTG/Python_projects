def read_graph():
	N = int(input())
	M = int(input())
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
	return graph, N, M

def checking(This, others, checked):
	checked.append(This)
	for other in others[This]:
		if other not in checked:
			checking(other, others, checked)
	return checked

def turn(graph, n):
	GRAPH = [[] for i in range(n)]
	for i in range(n):
		for j in graph[i]:
			GRAPH[j].append(i)
	return GRAPH

def shot(graph, n):
	numb = -1
	used = []
	for that in range(n):
		if that not in used:
			checking(that, graph, used)
			numb += 1
	return numb

graph, n, m = read_graph()
numb = shot(graph, n)
GRAPH = turn(graph, n)
count = shot(GRAPH, n)

if n == 1 and m == 0:
	print("YES")
elif numb == count:
	print("YES")
else:
	print("NO")