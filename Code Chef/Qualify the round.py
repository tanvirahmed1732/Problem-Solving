# cook your dish here
for _ in range(int(input())):
    x,a,b=map(int,input().split())
    if x<=((a*1)+(b*2)):
        print("Qualify")
    else:
        print("NotQualify")
