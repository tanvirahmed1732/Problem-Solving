# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(str,input().split()))
    a,b=0,0
    for i in lst:
        if i[0] == "S":
            a+=1
        else:
            b+=1
    print(a,b)
