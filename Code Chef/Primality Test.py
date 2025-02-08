# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n == 1:
        print("no")
    else:
        flag=True
        for i in range(2,n//2+1):
            if n%i==0:
                flag=False
                break
        if flag:
            print("yes")
        else:
            print("no")
