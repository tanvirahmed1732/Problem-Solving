Prime Reversal
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))
    counta = 0 
    countb = 0
    for j in range(n):
        if(a[j] == 1):
            counta +=1
        if(b[j] == 1):
            countb += 1
    if(counta == countb):
        print('YES')
    else:
        print('NO')
