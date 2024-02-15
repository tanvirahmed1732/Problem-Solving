# The Attack of Queen
for _ in range(int(input())):
    n,x,y = map(int, input().split())
    c = 0
    # these are for diagonal count.
    c+=n-x
    c+=y-1
    c+=x-1
    c+=n-y
    #these are for corner count.
    c+=min(x-1,y-1)
    c+=min(x-1,n-y)
    c+=min(n-x,y-1)
    c+=min(n-x,n-y)
    
    print(c)
