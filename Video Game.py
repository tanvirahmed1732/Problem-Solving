# Video Game
n,h = map(int,input().split())
st = list(map(int,input().split()))
ins = list(map(int,input().split()))
j = 0
k = 0
for i in ins:
    match i:
        case 1 if j != 0:
            j -= 1
        case 2 if j != (n-1):
            j += 1 
        case 3 if k != 1:
            if st[j] != 0:
                k = 1 
                st[j] -= 1 
        case 4 if k != 0:
            if st[j] != h:
                st[j] += 1 
                k = 0
        case 0:
            break 
print(*st)
