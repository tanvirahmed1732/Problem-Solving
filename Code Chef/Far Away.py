# Far Away
for _ in range(int(input())):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 0
    for i in lst:
        if i>(m//2): # if it is greater than half of the m
            count += i -1 # then we substruct 1. because it will be maximum
        else:
            count += m-i # otherwise m-i. and store the sum in count.
    print(count)
