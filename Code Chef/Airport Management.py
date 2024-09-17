# https://www.codechef.com/problems/AIRM
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.extend(list(map(int,input().split())))
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(max(dic.values()))
