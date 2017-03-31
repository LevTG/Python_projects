def cmp(s, sub):
	len_s = len(s)
	len_sub = len(sub)
	pos = 0
	while pos + len_sub <= len(s):
		found = True
		i = 0
		while i < len_sub:
			if s[pos + i] != sub[i]:
				found = False
				break
			i += 1
		if found:
			break
		pos += 1
	else:
		pos = -1
	return pos

A = 'opso'
B = 'opm'

print(cmp(A,B))