# Card Swipe
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    tlst = set()
    mx = 0
    for i in range(n):
        if lst[i] not in tlst:
            tlst.add(lst[i])
        else:
            tlst.remove(lst[i])
        mx = max(mx, len(tlst))
    print(mx)
