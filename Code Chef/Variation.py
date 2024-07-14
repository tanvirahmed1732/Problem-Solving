# Variation
n,k = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if abs(lst[i] - lst[j]) >= k:
            count +=1 
print(count)
