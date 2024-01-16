# Download file
for _ in range(int(input())):
    n,k = map(int, input().split())
    temp = 0
    for i in range(n):
        t,d = map(int, input().split())
        if k != 0:
            if t>k:
                t = t - k 
                temp = temp + t * d
                k = 0
            else:
                k = k - t 
        else:
            temp = temp + t * d 
    print(temp)
