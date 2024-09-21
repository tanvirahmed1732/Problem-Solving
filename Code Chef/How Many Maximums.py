# https://www.codechef.com/problems/HOWMANYMAX
for _ in range(int(input())):
    n=int(input())
    lst=input()
    ar=[True]*n
    for i in range(n-1):
        if lst[i]=='0':
            ar[i]=False
        else:
            ar[i+1]=False
    print(ar.count(True))
