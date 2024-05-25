# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    md = lst[0]%lst[1]
    for i in range (2,n):
        md=md%lst[i]
    print(md)
