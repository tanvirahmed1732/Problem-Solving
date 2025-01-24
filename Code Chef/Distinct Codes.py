# https://www.codechef.com/problems/DISTCODE
for _ in range(int(input())):
    s=input()
    ans=0
    a=[]
    for i in range(len(s)-1):
        if s[i:i+2] not in a:
            a.append(s[i:i+2])
            ans+=1
    print(ans)
