# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print("yes" if y>=x/2 else "no")
