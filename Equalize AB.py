# Equalize AB
for _ in range(int(input())):
    a,b,x = map(int, input().split())
    print('YES' if a == b else 'YES' if (a-b)%(x*2) == 0 else 'NO')
    # here if the difference between a and b is dibisible by x*2 then after
    # performing some given operation we make a=b. 
