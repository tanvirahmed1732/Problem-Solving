# https://www.codechef.com/problems/TWOTRAINS?tab=statement
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    print(max(lst)+sum(lst))
