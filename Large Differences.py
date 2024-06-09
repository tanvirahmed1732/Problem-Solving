# Large Differences
for _ in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    m=0
    b=lst[:n]
    for i in range(n):
        s=0
        b[i] = 1
        for j in range(n-1):
            s+=abs(b[j]-b[j+1])
        if m<s:
            m=s
        b[i] = k 
        s=0
        for j in range(n-1):
            s+=abs(b[j]-b[j+1])
        if m<s:
            m=s 
        b=lst[:n]
    print(m)
