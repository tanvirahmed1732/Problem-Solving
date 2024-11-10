# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=a+b
    s=s//2
    if s%2==0:
        print("Alice")
    else:
        print("Bob")
