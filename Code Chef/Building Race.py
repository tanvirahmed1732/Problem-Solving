# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    at=a/x
    bt=b/y  
    if at==bt:
        print("Both")
    elif at<bt:
        print("Chef")
    else:
        print("Chefina")
        
