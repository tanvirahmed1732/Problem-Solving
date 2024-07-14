# Max Nutrition
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    temp=[0]*n
    s=0
    for i in range(n):
        if b[i]>0 and temp[a[i]-1]<b[i]:
            temp[a[i]-1] = b[i]
    print(sum(temp))
