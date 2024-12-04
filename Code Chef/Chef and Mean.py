# https://www.codechef.com/problems/CHFM
import statistics as st
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    tem=st.mean(lst)
    if tem in lst:
        print(lst.index(tem)+1)
    else:
        print("Impossible")
