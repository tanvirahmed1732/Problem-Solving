# Hostel Room
for _ in range(int(input())):
    n,x = map(int, input().split())
    lst = list(map(int,input().split()))
    mx = x
    temp = x
    for i in lst:
        mx += i
        if mx>temp:
            temp = mx 
    print(temp)
