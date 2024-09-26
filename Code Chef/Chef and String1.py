# https://www.codechef.com/problems/RECNDSTR?tab=statement
for _ in range(int(input())):
    st=input()
    if st[1:]+st[0] == st[-1]+st[:-1]:
        print("YES")
    else:
        print("NO")
