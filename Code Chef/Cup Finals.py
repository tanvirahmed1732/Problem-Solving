# cook your dish here
for _ in range(int(input())):
    x,y,d=map(int,input().split())
    print("YES" if abs(x-y)<=d else "NO")
