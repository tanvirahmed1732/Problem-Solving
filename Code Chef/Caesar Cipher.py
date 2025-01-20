# https://www.codechef.com/problems/CAESAR
for _ in range(int(input())):
    n=int(input())
    s,t,u=input(),input(),input()
    x=ord(t[0])-97
    y=ord(s[0])-97
    k=(x-y+26)%26
    ans=''
    for i in u:
        temp=ord(i)-97
        temp=(temp+k)%26
        temp+=97
        ans+=chr(temp)
    print(ans)
