# Group Assignment
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst1 = set(lst) #for time complexity
    check = False
    for i in lst1: # here we check for all elements in the set.
        if lst.count(i)% i != 0: # if the wanted group is not available then we print no. Otherwise, print yes.
            check = True
            break
    if check:
        print('NO')
    else:
        print('YES')
