def read_plan():
	n, m = [int(x) for x in input().split()]
	plan = []
	for i in range(m):
		a, b = [int(x) for x in input().split()]
		plan.append((a, b))
	return n, m, plan

def checking(This, others, checked = set()):
	checked.add(This)
	for other in others[This]:
		if other not in checked:
			checking(other, others, checked)
	return checked

def add_bridge(num, plan, graph):
	a, b = plan[num]
	graph[a].append(b)
	graph[b].append(a)

n, m, plan = read_plan()
graph = [[] for i in range(n)]

for i in range(m):
	add_bridge(i, plan, graph)
	noc = 0
	used = set()
	for that in range(n):
		if that not in used:
			checking(that, graph, used)
			noc += 1
	if noc == 1:
		print(i + 1)
		exit()