# cook your dish here
import math 
for _ in range(int(input())):
    n = int(input())
    c = 0
    while n != 0:
        m = int(math.sqrt(n))
        #print(m)
        c+=1
        n=n-(m*m)
    print(c)
