# Chef and Glove
for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    g = list(map(int, input().split()))
    front = True
    back = True
    for i in range(n):
        if f[i]>g[i]:
            front = False
        if f[i]>g[n-1-i]:
            back = False
    if front and back:
        print('both')
    elif front:
        print('front')
    elif back:
        print('back')
    else:
        print('none')
