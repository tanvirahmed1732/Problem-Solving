# Dividing Stamps
n = int(input())
lst=list(map(int,input().split()))
sm=0
for i in range(1,n+1):
    sm+=i
if sum(lst) == sm:
    print("YES")
else:
    print("NO")
