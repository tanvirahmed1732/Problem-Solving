# https://www.codechef.com/problems/MODEFREQ
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    freq=[0]*11
    for i in lst:
        freq[i]+=1
    # print(*freq)
    freq2=[0]*(max(freq)+1)
    for i in freq:
        freq2[i]+=1
    # print(*freq2)
    mx=-1
    ans=0
    for i in range(1,len(freq2)):
        if freq2[i]>mx:
            mx=freq2[i]
            ans=i
    print(ans)
