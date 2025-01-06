# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    if n%2!=0:
        print(-1)
    else:
        m=abs(sum(lst))
        print(m//2)
    
