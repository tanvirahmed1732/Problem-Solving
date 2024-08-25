# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=0
    while n!=0:
        temp=n%10
        n=n//10
        a*=10
        a+=temp
    print(a)
