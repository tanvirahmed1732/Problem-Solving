# Rectangle in python
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a !=b and a != c and a != d:
        print('NO')
    elif a == b and c != d:
        print('NO')
    elif a == c and b != d:
        print('NO')
    elif a == d and b != c:
        print('NO')
    else:
        print('YES')
