# cook your dish here
for _ in range (int(input())):
    n=int(input())
    s=input()
    ans=""
    for i in s:
        if i == 'A':
            ans+='T'
        elif i == 'T':
            ans+='A'
        elif i=='G':
            ans+='C'
        else:
            ans+='G'
    print(ans)
