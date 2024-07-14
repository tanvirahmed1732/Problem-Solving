# Football Ties
for _ in range(int(input())):
    x,y = map(int,input().split())
    z = max(x,y)
    print(z%3)
