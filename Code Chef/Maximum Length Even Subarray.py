# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MXEVNSUB
for _ in range(int(input())):
    n=int(input())
    if n == 1:
        print(0)
    elif (n-1)%4==0:
        print(n-1)
    elif n%2==0 and n%4!=0:
        print(n-1)
    else:
        print(n)
