# Chef and Steps
for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    s = ''
    for i in lst:
        if i % k == 0:
            s = s + '1'
        else:
            s = s + '0'
    print(s)
