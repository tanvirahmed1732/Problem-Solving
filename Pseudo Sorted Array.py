# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    count = 0
    sort = sorted(lst)
    for i in range(n-1):
        if(lst[i]>lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i] 
            break
    if(lst != sort):
        print('NO')
    else:
        print('YES')
        
