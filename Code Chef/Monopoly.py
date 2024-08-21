# cook your dish here
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    for i in lst:
        if (sum(lst)-i)<i:
            print("YES")
            break
    else:
        print("NO")
