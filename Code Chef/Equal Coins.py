# https://www.codechef.com/problems/EQUALCOIN
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0 and b%2!=0:
        print("NO")
        continue
    if a%2==1:
        print("NO")
    else:
        print("YES")
