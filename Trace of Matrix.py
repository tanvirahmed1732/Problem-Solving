#Trace of Matrix
for _ in range(int(input())):
    n = int(input())
    lst = list()
    mx = 0
    for i in range(n):
        lst.append(list(map(int, input().split())))
        
    for i in range(n):
        a = 0
        for j in range(n-i):
            a += lst[j+i][j]
        mx = max(a, mx)
        
    for i in range(1, n):
        a = 0
        for j in range(n-i):
            a += lst[j][i+j]
        mx = max(a, mx)
        
    print(mx)
