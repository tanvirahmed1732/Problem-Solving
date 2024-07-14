# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    count = 0
    for i in lst:
        count += i
    if(count % 2 == 0):
        print('NO')
    else:
        print('YES')
