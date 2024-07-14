# Janmansh at Fruit Market
for _ in range(int(input())):
    x,a,b,c=map(int,input().split())
    lst=[a,b,c]
    lst.sort()
    print((x-1)*lst[0] + lst[1])
