# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if(n == 50):
        print(0)
    elif n < 50:
        if n%2 == 0:
            print((50-n)//2)
        else:
            print((50-n)//2+3)
    else:
        if (n-50)%3==0:
            print((n-50)//3)
        elif (n-50)%3==1:
            print((n-50)//3+2)
        elif (n-50)%3==2:
            print((n-50)//3+4)
