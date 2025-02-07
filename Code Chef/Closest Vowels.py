# cook your dish here
for _ in range(int(input())):
    n=int(input())
    st=input()
    temp='clrg'
    ans=1
    for i in st:
        if i in temp:
            ans = 2*ans
    print(ans%(10**9+7))
