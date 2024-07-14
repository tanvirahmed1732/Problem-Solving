# Convert to permutation
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    m = (n*(n+1))//2 # it is the formula of summation a series of size n.
    temp = True
    for i in range(n):
        if lst[i]>i+1: #after sorting if there is any Ai element is greter than i then it is not possible to convert to permutation. 
            temp = False # for example 0 3 3 there is 3 in 2th position so it is not posible to convert.
            break
    print(-1 if temp == False else m - sum(lst)) # to find the operation required here I subtruct sum of the lst 
    # from the actual series theat is required to convert. from this we will get the actual operation needed.
