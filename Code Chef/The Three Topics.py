# cook your dish here
lst=list(map(int,input().split()))
if lst[3] in lst[:3]:
    print("Yes")
else:
    print("No")
