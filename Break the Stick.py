# Break the Stick
for i in range(int(input())):
    n, x = map(int,input().split())
    if(n%2==0 or x%2==1):
        print("YES")
    else:
        print("NO")
