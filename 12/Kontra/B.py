def cxema(path):
	for x in path:
		print(''.join([dask[x[0]], str(x[1] + 1)]))

def neighbour(cnt):
	others = []
	val = set()
	x = cnt[0]
	y = cnt[1]
	val.add((x - 1, y - 2))
	val.add((x - 1, y + 2))
	val.add((x - 2, y - 1))
	val.add((x - 2, y + 1))
	val.add((x + 2, y + 1))
	val.add((x + 2, y - 1))
	for i in val:
		if 7 >= i[0] >= 0 and 7 >= i[1] >= 0:
			others.append(i)
	return others

horizontal = [0, 1, 2, 3, 4, 5, 6, 7]
vertical = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Dask = dict(zip(vertical, horizontal))
dask = dict(zip(horizontal, vertical))

pos = input()
start = (Dask[pos[0]], int(pos[1]) - 1)

W = [start]
used = set()
path = {start: [start]}

v = input()
end = (Dask[v[0]], int(v[1]) - 1)

while W:
	cur = W.pop(0)
	for s in neighbour(cur):
		if s not in used:
			W.append(s)
			new_path = path[cur] + [s]
			if s not in path or len(new_path) < len(path[s]):
				path[s] = new_path
			if s == end:
				cxema(path[end])
				exit(0)