# A Balanced Contest
for _ in range(int(input())):
    n,p = map(int, input().split())
    lst = list(map(int, input().split()))
    e,d = 0,0
    for i in lst:
        if (i<=p//10):
            d += 1
        if (i>= p//2):
            e += 1
    if (e ==1 and d == 2):
        print('yes')
    else:
        print('no')
