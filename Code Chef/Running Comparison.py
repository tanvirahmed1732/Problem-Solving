t = int(input())

while t > 0:
    count = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if 2*a[i]<b[i] or 2*b[i]<a[i]:
            count+=1
    print(n-count)
    t -= 1
