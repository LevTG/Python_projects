def read_graph():
    N, M = [int(x) for x in input().split()]
    graph = {i:{} for i in range(N)}
    for j in range(M):
        a, b, c = [int(x) for x in input().split()]
        graph[a][b] = c
        graph[b][a] = c
    return graph, N, M

def hamilton(graph, n, v = 0, used = None, path = None):
    if not used:
        used, path = {v}, []
    path.append(v)
    if len(path) == n:
        if path[0] in graph[path[-1]]:
            return True, path
        else:
            path.pop()
            return False, path
    used.add(v)
    for i in graph[v]:
        if i not in used:
            if hamilton(graph, n, i, used, path)[0]:
                return True, path
    used.remove(v), path.pop()
    return False, path

def get_sum(path, graph, n):
    summary = 0
    for i in range(-1, n - 1):
        summary += graph[path[i]][path[i + 1]]
    return summary
 
graph, n, m = read_graph()
min_sum = 10**9
for vertex in graph:
    is_ham, path = hamilton(graph, n, vertex)
    if is_ham:
        summary = get_sum(path, graph, n)
        min_sum = min(min_sum, summary)

print(min_sum)
print(" ".join(map(str, path)))