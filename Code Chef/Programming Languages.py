# cook your dish here
for _ in range(int(input())):
    lst=list(input().split())
    if (lst[0],lst[1])==(lst[2],lst[3]) or (lst[0],lst[1])==(lst[3],lst[2]):
        print(1)
    elif (lst[0],lst[1])==(lst[4],lst[5]) or (lst[0],lst[1])==(lst[5],lst[4]):
        print(2)
    else:
        print(0)
