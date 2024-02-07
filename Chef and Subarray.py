# Chef and Subarray
n = int(input())
lst = list(map(int, input().split()))
temp = True
count = 0
mx = 0
for i in range(n):
    if lst[i] == 0:
        temp = False
        if mx<count:
            mx = count
        count = 0
    else:
        count += 1
if temp == True:
    mx = n
print(mx)
