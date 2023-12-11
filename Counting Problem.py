# Counting Problem
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    count = 0
    for i in lst:
        if i%2 == 1:
            count += 1 
    if count % 2 == 0 and count != 0:
        print('YES')
    else:
        print('NO')
