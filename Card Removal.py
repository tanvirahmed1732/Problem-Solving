# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    frq = [0] * 11
    for i in lst:
        frq[i] += 1
    mx = 0
    for i in range(1,11):
        if mx < frq[i]:
            mx = frq[i]
    print(n-mx)
