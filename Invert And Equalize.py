# Invert And Equalize
for _ in range(int(input())):
    n = int(input())
    st = input()
    n0=0
    n1=0
    temp = st[0]
    if temp == '0':
        n0+=1
    else:
        n1+=1
    for i in st:
        if i != temp:
            if i == '0':
                n0+=1
            else:
                n1+=1
            temp = i
    print(min(n0,n1))
