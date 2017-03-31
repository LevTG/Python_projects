A = list(map(str, input().split()))
x = int(bin(int(A[0], 16)), 2)
y = int(bin(int(A[1], 16)), 2)
S = hex(x^y)
print(S[2:])

