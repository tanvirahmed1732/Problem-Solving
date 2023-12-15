# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    st ={}
    for i in lst:
        if i in st:
            st[i] += 1
        else:
            st[i] = 1
    print(n-(max(st.values())))
