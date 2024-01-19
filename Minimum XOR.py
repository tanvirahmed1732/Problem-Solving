# Minimum XOR
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    m = 0
    for i in range(n):
        m = m ^ lst[i]
    if m == 0:
        print(m)
    else:
        temp = m
        for i in range(n):
            temp = min(temp, m ^ lst[i])
        print(temp)
