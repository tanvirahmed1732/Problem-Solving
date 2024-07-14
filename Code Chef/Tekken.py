# Tekken
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print('YES' if 0< a-abs(b-c) else 'NO')
