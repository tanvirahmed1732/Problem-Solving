# cook your dish here
for _ in range (int(input())):
    n,a,b = map(int,input().split())
    s=str(input())
    k=s.count('0')
    print(k*a + (n-k)*b)
