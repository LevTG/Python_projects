A = list(map(int, input().split()))
price = A[0]
delta = A[1]
m = A[2]
print((2*price + delta*(m*7 - 1))*m*7//2)