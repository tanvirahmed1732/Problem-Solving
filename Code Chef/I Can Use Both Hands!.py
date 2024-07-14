# I Can Use Both Hands!
import math
for _ in range(int(input())):
    l,r,m=map(int,input().split())
    print(math.ceil(m/l)+m//r)
