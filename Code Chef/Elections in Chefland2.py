# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    lst=list(map(int,input().split()))
    c=0
    for i in lst:
        if i>=x:
            c+=1 
    print(c)
