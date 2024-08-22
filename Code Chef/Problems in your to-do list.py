# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int, input().split()))
    c=0
    for i in lst:
        if i>=1000:
            c+=1
    print(c)
