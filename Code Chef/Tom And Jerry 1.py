# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TANDJ1
for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    temp=abs(c-a) + abs(d-b)
    if k>=temp:
        if temp%2==0 and k%2==0:
            print("YES")
        elif temp%2==1 and k%2==1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
