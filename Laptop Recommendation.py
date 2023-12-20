# Laptop Recommendation
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    f = {}
    for i in lst:
        if i in f:
            f[i] += 1 
        else:
            f[i] = 1 
    #print(f)
    # f = list(f)
    mx = max(f.values())
    #print(mx)
    ch = 0
    for i in f.values():
       if mx == i:
           ch = ch + 1
    if ch  == 1:
        print(list(f.keys())[list(f.values()).index(mx)])
    else:
        print('CONFUSED')
