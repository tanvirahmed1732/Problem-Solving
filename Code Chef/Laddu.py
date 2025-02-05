# cook your dish here
for _ in range(int(input())):
    n,o=map(str,input().split())
    ans=0
    for i in range(int(n)):
        st=input()
        if "CONTEST_WON" in st:
            t=int(st[12:])
            if t<20:
                ans=ans+300+20-t
            else:
                ans+=300
        if st == "CONTEST_HOSTED":
            ans+=50
        if st == "TOP_CONTRIBUTOR":
            ans+=300
        if "BUG_FOUND" in st:
            t=int(st[10:])
            ans+=t 
    if o == "INDIAN":
        print(ans//200)
    else:
        print(ans//400)
