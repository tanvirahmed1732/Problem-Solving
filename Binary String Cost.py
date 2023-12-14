# Binary String Cost
for _ in range(int(input())):
    n,x,y = map(int, input().split())
    s = input()
    c0 = s.count('0')
    c1 = s.count('1')
    if(c0 > 0  and c1 > 0):
        if(x<y):
            print(x)
        else:
            print(y)
    else:
        print(0)
