# cook your dish here
for i in range(int(input())):
    n , x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for j in range(n):
        if(a[j]>= x):
            count += b[j]
    print(count)
