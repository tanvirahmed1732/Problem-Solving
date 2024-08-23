# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a>b or c>b:
        print('no')
    else:
        print('yes')
