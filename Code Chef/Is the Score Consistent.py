# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    print("POSSIBLE" if a<=c and b<=d else "IMPOSSIBLE")
