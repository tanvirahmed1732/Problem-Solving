# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/IMDB
for _ in range(int(input())):
    n,x=map(int,input().split())
    ans=-1
    for i in range(n):
        sp,im=map(int,input().split())
        if sp<=x:
            if im>ans:
                ans=im
    print(ans)
