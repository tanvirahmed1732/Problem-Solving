# Make Money
for _ in range(int(input())):
    n,x,c = map(int, input().split())
    lst = list(map(int, input().split()))
    xc = x - c
    count = 0
    for i in range(n):
        if(lst[i]<xc):
            lst[i] = x 
            count+=1
    summ = 0
    for i in lst:
        summ += i
    summ = summ - (c*count)
    print(summ)
