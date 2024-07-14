# Easy Math
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    mx = 0
    for i in range(n-1):
        for j in range(i+1, n):
            m = s[i] * s[j] 
            sm = 0
            for k in str(m):
                sm += int(k)
            if mx<sm:
                mx = sm 
    print(mx)
