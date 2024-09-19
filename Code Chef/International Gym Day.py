# https://www.codechef.com/problems/GYMDAY?tab=statement
for _ in range(int(input())):
    d,x,y=map(int,input().split())
    if y>=x:
        print(0)
        continue
    a=x
    c=0
    while(y!=0):
        c+=1 
        y-=1
        x=a-((a*c*d)/100)
        if x<=y:
            print(c)
            break
    else:
        print(-1)
