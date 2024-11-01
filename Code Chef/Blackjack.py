# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(21-a-b if 21-a-b<=10 else -1)
