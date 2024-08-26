# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFRICH
import math
for _ in range(int(input())):
    a,b,x=map(int,input().split())
    print(math.ceil((b-a)/x))
