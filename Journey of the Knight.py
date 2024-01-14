# Journey of the Knight
for _ in range(int(input())):
    w,x,y,z = map(int, input().split())
    temp = (w-x) + (y - z)
    if temp % 2 == 0:
        print('YES')
    else:
        print('NO')
