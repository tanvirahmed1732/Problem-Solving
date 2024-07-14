# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    print('YES' if (a == b and a<=c) else 'YES' if (a == c and a<=b) else 'YES' if (b==c and b<=a) else 'NO')
