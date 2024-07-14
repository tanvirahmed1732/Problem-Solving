# Ups and Downs
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if i%2 == 0: # if the position is even
            if a[i]>a[i+1]: # checking the opposite condition. 
                a[i],a[i+1] = a[i+1],a[i] # if true the we simply swap then we get the currect condition
        else: # if the position is odd. we are doing same here.
            if a[i]<a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    print(*a) # printing all elemnet in the list.
