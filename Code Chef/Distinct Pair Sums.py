# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MANYSUMS
for _ in range(int(input())):
    i,j=map(int,input().split())
    d=j-i+1
    print((d*2)-1)
