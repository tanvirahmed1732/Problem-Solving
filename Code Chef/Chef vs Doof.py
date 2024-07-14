# Chef vs Doof
for _ in range(int(input())):
    n = int(input())
    lst=list(map(int,input().split()))
    for i in lst:
        if i%2==0:
            print("NO")
            break
    else:
        print("YES")
