# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    if n%2==0:
        print(sum(lst[:n//2])-sum(lst[n//2:]))
    else:
        print(sum(lst[:(n//2)+1])-sum(lst[(n//2)+1:]))
