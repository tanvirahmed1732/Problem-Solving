# Max Binary
for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    if s[0] == '0':
        s = '1' + s[1:]
        k -=1 
        
    s = s + k*'0'
    print(s)
