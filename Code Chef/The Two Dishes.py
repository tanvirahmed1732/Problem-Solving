# https://codechef.com/practice/course/1to2stars/LP1TO201/problems/MAX_DIFF
for _ in range(int(input())):
    n,k=map(int,input().split())
    m=min(n,k)
    for i in range(m+1):
        if (m+i)==k:
            print(m-i)
            break
