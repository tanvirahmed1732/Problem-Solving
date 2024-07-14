# Count of Maximum
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    mx = max(freq.values())
    mn = 10001
    for i in freq:
        if freq[i]==mx:
            if i <= mn:
                mn = i
    print(mn,mx)
