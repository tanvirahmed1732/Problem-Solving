# https://www.codechef.com/problems/OJUMPS
a=int(input())
a=a%6
if a==0 or a==1 or a==3:
    print("yes")
else:
    print("no")
