# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    ans=((n//2)*a)+((n//2)*b)
    print(ans if n%2==0 else ans+b)
