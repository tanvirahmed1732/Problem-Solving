# Candies
t= int(input())
while(t>0):
    n = int(input())
    ar=list(map(int,input().split()))
    check = True
    for i in ar:
        if(ar.count(i)>2):
            check = False
            break
    if(check == True):
        print("YES")
    else:
        print("NO")
    t = t - 1
