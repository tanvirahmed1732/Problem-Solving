# cook your dish here
mx=-1
ans=0
a,b=0,0
for _ in range(int(input())):
    x,y=map(int,input().split())
    a+=x
    b+=y
    if a>b:
        if mx<a-b:
            mx=a-b
            ans=1
    else:
        if mx<b-a:
            mx=b-a
            ans=2
print(ans,mx)
