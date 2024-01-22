# Make Multiple
import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = int(b/2)
    if(a == b):
        print('YES')
    elif(a<=c):
        print('YES')
    else:
        print('NO')
