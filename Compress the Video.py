# Compress the Video
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    if n == 1:
        print(n)
    elif n == 2:
        if lst[0] == lst[1]:
            print(1)
        else:
            print(n)
    else:
        i=0
        temp=n
        while(i<n):
            if i<n-1 and lst[i] == lst[i+1]:
                temp-=1
            i+=1
        print(temp)
            
