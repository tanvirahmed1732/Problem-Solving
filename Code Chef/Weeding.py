# cook your dish here
for _ in range(int(input())):
    n,m,k = map(int,input().split())
    lst = list(map(int,input().split()))
    t = True
    for i in lst:
        if k+i > m+1:
            t = False
    if t:
        print('yes')
    else:
        print('no')
