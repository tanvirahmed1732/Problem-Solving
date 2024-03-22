# Permutation Disturbance
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    i = 1
    c = 0
    while(i<=n):
        if i!=n and (lst[i] == i+1) and (lst[i-1] == i):
            c +=1 
            i +=2
        elif lst[i-1] == i:
            c+=1
            i+=1
        else:
            i += 1
    print(c)
