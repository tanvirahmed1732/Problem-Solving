# cook your dish here
for _ in range(int(input())):
    a,b,c,d,n=map(int,input().split())
    temp=b-a
    temp=temp/n
    print(1 if temp>=c and temp<=d else 0)
