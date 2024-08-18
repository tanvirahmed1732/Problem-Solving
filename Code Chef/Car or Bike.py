# cook your dish here
for _ in range(int(input())):
    c,b=map(int,input().split())
    if c==b:
        print("SAME")
    elif c>b:
        print('CAR')
    else:
        print("BIKE")
