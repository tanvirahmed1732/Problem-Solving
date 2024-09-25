# https://www.codechef.com/problems/STUDVOTE?tab=statement
for _ in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    dic={}
    for i in lst:
        if i not in dic:
            dic[i]=1 
        else:
            dic[i]+=1
    c=0
    #print(dic)
    for j in dic:
        if dic[j]>=k and lst[j-1]!=j:
            c+=1
    print(c)
