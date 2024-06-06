# Xenny and Alternating Tasks
for _ in range(int(input())):
    n = int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    s1=0
    s2=0
    for i in range(n):
        if (i+1)%2==0:
            s1+=x[i]
            s2+=y[i]
        else:
            s1+=y[i]
            s2+=x[i]
    print(min(s1,s2))
