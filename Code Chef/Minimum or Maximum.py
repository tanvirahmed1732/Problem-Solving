# https://www.codechef.com/problems/MINORMAX
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    mx=lst[0]
    mn=lst[0]
    for i in lst:
        if i>mn and i<mx:
            print("NO")
            break
        elif i<mn:
            mn=i
        elif i>mx:
            mx=i
    else:
        print("YES")
