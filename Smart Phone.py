# Smart Phone
n = int(input())
lst = []
for i in range(n):
    lst.insert(i,int(input()))
lst.sort()
mx = 0
for i in range(n):
    if (lst[i] * (n - i)) > mx:
        mx = lst[i] * (n-i)
print(mx)
