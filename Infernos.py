# Infernos
import math
for _ in range(int(input())):
    n,x = map(int,input().split())
    lst = list(map(int,input().split()))
    s = 0
    for i in lst:
        if i<=x:
            s += 1
        else:
            s += math.ceil(i/x)
    m = max(lst)
    print(m if m<s else s)
