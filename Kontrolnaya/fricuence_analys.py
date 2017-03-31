N = int(input())
A = list(map(int, input().split()))

middle = 0

Dict = {}

for thing in A:
	if thing not in Dict:
		Dict[thing] = 1
	else:
		Dict[thing] += 1

val = Dict.values()

print(val.count(max(val)))

for v in val:
	if middle < v < max(val):
		middle = v
		
print(val.count(middle))
