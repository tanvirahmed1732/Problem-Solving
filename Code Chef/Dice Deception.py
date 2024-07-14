# cook your dish here
for _ in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    i = 0
    j = 0
    while(i<n):
        if lst[i]<4:
            lst[i] = 7 - lst[i]
            j+=1
        if j == k:
            break
        i+=1
    print(sum(lst)) 
