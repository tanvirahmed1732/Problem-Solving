# Sale
for _ in range (int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    sm = 0
    for i in lst:
        sm += i
        if (sm + i) > mx:
            mx = sm + i
    print(mx)
