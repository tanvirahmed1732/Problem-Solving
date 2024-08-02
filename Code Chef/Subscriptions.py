# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUBSCRIBE_
import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    print(math.ceil(n/6)*x)
