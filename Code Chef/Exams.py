# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int, input().split())
    print('YES' if (x*y)/2<z else "NO")
