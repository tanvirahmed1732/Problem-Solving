# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    odd = 0
    for i in lst:
        if(i%2==1):
            odd +=1
    # print(odd)
    if(n==1):
        print(1)
    elif(odd%2==0 or odd == 0):
        print(1)
    else:
        print(2)
