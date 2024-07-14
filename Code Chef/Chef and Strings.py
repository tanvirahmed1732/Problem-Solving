# Chef and Strings
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        count += abs(lst[i]-lst[i+1]) -1
    print(count)
