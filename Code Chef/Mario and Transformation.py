# cook your dish here
for _ in range(int(input())):
    x=int(input())
    n=x%3
    print("NORMAL" if n==0 else "HUGE" if n==1 else "SMALL")
