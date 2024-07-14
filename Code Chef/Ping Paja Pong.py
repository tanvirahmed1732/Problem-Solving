# Ping Paja Pong
for _ in range(int(input())):
    x,y,k=map(int, input().split())
    if ((x+y)//k)%2:
        print("Paja")
    else:
        print("Chef")
