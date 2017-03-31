B = list(map(int, input(). split()))
n = B[0]
m = B[1]
A = []
C = []
for i in range(n):
    A.append(list(map(int, input(). split())))
    D = [max(A[i]), A[i].index(max(A[i]))]
    C.append(D)
print(C.index(max(C)), C[C.index(max(C))][1])

