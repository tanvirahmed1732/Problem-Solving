# Lazy Jem
for _ in range(int(input())):
    n,b,m = map(int,input().split())
    time = 0
    mul = 1
    while(n>0):
        if(n%2 == 1):
            x = int((n+1)/2)
            time += x*m*mul
            time += b 
            n -= x
        else:
            x = int(n/2)
            time += x*m*mul
            time += b 
            n -= x
        mul *= 2
    print(time-b)
