# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    temp=(y-1)//10 - (x-1)//10
    print(abs(temp))
