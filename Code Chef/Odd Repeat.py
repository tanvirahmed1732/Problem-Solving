# https://www.codechef.com/problems/REPEAT?tab=statement
for _ in range(int(input())):
    n,k,s=map(int,input().split())
    print((s-n**2)//(k-1))
# n^2+(k-1)*x=s
# or, x*(k-1)=s-n^2
# or, x=(s-n^2)//(k-1)
