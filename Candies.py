# cook your dish here
t= int(input())
while(t>0):
    n = int(input())
    ar = []
    check = True
    for i in range(2*n):
        ar.append(int(input()))
    for i in ar:
        if(ar.count(i)>2):
            check = False
            break
    if(check == True):
        print("YES")
    else:
        print("NO")
    t = t - 1