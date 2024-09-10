# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/NFS
import math
for _ in range(int(input())):
    u,V,a,s=map(int,input().split())
    if u<=V:
        print("Yes")
        continue
    v=(u*u)-(2*a*s)
    if v<0:
        print("Yes")
        continue
    v=math.sqrt(v)
    if v>V:
        print("No")
    else:
        print("Yes")
