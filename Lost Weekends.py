# Lost Weekends
for _ in range(int(input())):
    lst = list(map(int,input().split()))
    summ = 0
    for i in range(5):
        summ += lst[i]
    if((summ*lst[5])>120):
        print('Yes')
    else:
        print('No')
