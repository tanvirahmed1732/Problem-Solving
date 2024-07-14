# Change It
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    count = 0
    for i in lst:
        if(count<lst.count(i)):
            count = lst.count(i)
    print(n-count)
