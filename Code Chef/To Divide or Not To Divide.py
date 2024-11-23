# https://www.codechef.com/problems/DIVAB
import math
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    i=math.ceil(n/a)
    if a%b==0:
        print(-1)
    else:
        while 1:
            if (i*a)%b!=0:
                print(i*a)
                break
            i+=1
