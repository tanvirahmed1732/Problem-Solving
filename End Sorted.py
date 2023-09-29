# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    pn = lst.index(n)
    po = lst.index(1)
    if(pn<po):
        print(n-1-pn+po-1)
    else:
        print(n-1-pn+po)
