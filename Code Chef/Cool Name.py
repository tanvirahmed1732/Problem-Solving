# https://www.codechef.com/problems/CALPOWER
for _ in range(int(input())):
    s=input()
    s=sorted(s)
    ans=0
    for i in range(len(s)):
        ans+=(i+1)*(ord(s[i])-ord('a')+1)
    print(ans)
