def neighbour(vert):
	others = set()
	val = set()
	x = vert[0]
	y = vert[1]
	val.add((x - 1, y - 2))
	val.add((x - 1, y + 2))
	val.add((x - 2, y - 1))
	val.add((x - 2, y + 1))
	val.add((x + 2, y + 1))
	val.add((x + 2, y - 1))
	for i in val:
		if 0 <= i[0] <= 7 and 0 <= i[1] <= 7:
			others.add(i)
	return others

def Print(path):
	for x in path:
		print(''.join([dask[x[0]], str(x[1] + 1)]))

h = [0, 1, 2, 3, 4, 5, 6, 7]
v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Dask = dict(zip(v, h))
dask = dict(zip(h, v))

pos = input()
start = (Dask[pos[0]], int(pos[1]) - 1)

pos = input()
end = (Dask[pos[0]], int(pos[1]) - 1)


Q = [start]
used = set()
path = {start: [start]}

while Q:
	cur = Q.pop(0)
	
	for near in neighbour(cur):
		if near not in used:
			Q.append(near)
			new_path = path[cur] + [near]
			
			if near not in path or len(new_path) < len(path[near]):
				path[near] = new_path
			
			if near == end:
				Print(path[end])
				exit(0)