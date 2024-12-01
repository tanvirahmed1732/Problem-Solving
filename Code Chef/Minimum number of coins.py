# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x%5!=0:
        print(-1)
    elif x%10==0:
        print(x//10)
    else:
        print((x//10)+1)
