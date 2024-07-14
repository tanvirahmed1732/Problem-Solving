# Retrieve the Array
for _ in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))
    sm = sum(B)
    sm = sm//(n+1) #it is the sum(A) [sum(B)/n+1]
    A = list()
    for i in B:
        A.append(i-sm) # here Ai = Bi - sum(A)
    print(*A) #printing all element in A
