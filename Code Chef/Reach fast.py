# cook your dish here
import math
for _ in range(int(input())):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))
