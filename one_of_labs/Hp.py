x1 = int(input())
i = 0
if x1 == 0:
    pass
else:
    x2 = int(input())
    if x2 == 0:
        pass
    else:
        x3 = int(input())
    
        while x1 != 0 and x2 != 0 and x3 != 0:
            if x1 < x2 > x3:
                i += 1
            x1, x2, x3 = x2, x3, int(input())
print(i)