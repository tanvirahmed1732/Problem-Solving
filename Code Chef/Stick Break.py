# Stick Break
for _ in range(int(input())):
    l,k = map(int,input().split())
    if(l%k != 0):
        print(1)
    else:
        print(0)
