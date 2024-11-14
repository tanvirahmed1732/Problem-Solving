# https://www.codechef.com/problems/ROCPAPSCI
for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    i=0
    while i<n:
        if i<n-1 and s[i]==s[i+1]:
            i+=2
            ans+=1
        else:
            ans+=1
            i+=1
    print(ans)
