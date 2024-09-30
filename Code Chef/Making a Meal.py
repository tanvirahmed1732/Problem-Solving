# https://www.codechef.com/problems/CFMM
for _ in range(int(input())):
    n=int(input())
    fr={}
    for i in range(n):
        st=input()
        for j in st:
            if j in fr:
                fr[j]+=1
            else:
                fr[j]=1
    k="codechef"
    ans=0
    while 1:
        t=True
        for i in k:
            if i not in fr:
                t=False
                break
            if fr[i]==0:
                t=False
                break
            else:
                fr[i]-=1
        if t:
            ans+=1
        else:
            break
    print(ans)
