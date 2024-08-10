# cook your dish here
for _ in range(int(input())):
    n=int(input())
    print(n if n<=100 else n-25 if n<=1000 else n-100 if n<=5000 else n-500)
