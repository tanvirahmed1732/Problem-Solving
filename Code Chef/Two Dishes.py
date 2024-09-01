# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TWODISH
for _ in range(int(input())):
    n,a,b,c=map(int, input().split())
    temp=(a+c if a+c<=b else b)
    print('YES' if temp>=n else 'NO')
    
