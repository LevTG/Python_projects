def read_graph():
	N = int(input())
	M = int(input())
	graph = [[] for i in range(N)]
	for j in range(M):
		a, b = [int(x) for x in input().split()]
		graph[a].append(b)
		graph[b].append(a)
	return graph, N, M

def checking(This, others, checked = set()):
	checked.add(This)
	for other in others[This]:
		if other not in checked:
			checking(other, others, checked)
	return checked

List, n, m = read_graph()
if len(checking(0, List)) == n:
	print("YES")
else:
	print("NO")