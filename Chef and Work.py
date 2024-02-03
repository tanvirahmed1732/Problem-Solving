# Chef and Work
for _ in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = 0
    cnt = 0
    ct = False
    for i in range(n):
        if lst[i]>k:
            cnt = -2
            break
        if (temp + lst[i]) <=k:
            temp += lst[i]
        else:
            cnt += 1
            temp = lst[i]
    print(cnt+1)
