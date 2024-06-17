# Devu and an Array
n,q = map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
a=lst[0]
b=lst[n-1]
for _ in range(q):
    t=int(input())
    if t>=a and t<=b:
        print("Yes")
    else:
        print("No")
