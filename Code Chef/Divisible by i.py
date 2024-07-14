# Divisible by i
for _ in range(int(input())):
    n = int(input())
    i = n-2
    lst = list()
    lst.insert(0,n)
    lst.insert(0,1)
    while i>0:
        if n%2==0:
            if i % 2 == 0:
                lst.insert(0,(lst[0]+i))
            else:
                lst.insert(0,(lst[0]-i))
        else:
            if i % 2 == 0:
                lst.insert(0,(lst[0]-i))
            else:
                lst.insert(0,(lst[0]+i))
        i-=1
    print(*lst)
