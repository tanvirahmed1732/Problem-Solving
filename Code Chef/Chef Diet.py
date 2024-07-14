# Chef Diet
for i in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int,input().split()))
    for j in range(n):
        # print(j)
        if(k<=lst[j] and j != n -1):
            lst[j+1] = lst[j+1] + (lst[j] - k)
        elif(k<=lst[j] and j == n -1):
            print("YES")
        else:
            print("NO",j+1)
            break
