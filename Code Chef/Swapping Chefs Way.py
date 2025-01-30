# https://www.codechef.com/problems/SWAPCW
for _ in range(int(input())):
    n=int(input())
    s=input()
    lst=list(s)
    # print(lst)
    for i in range(n//2):
        if ord(s[i]) > ord(s[-i-1]):
            # print(i)
            lst[i],lst[-i-1]=s[-i-1],s[i]
        else:
            lst[i],lst[-i-1]=s[i],s[-i-1]
    if sorted(lst)==lst:
        print("YES")
    else:
        print("NO")
