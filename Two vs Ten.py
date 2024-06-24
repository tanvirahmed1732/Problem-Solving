# Two vs Ten
for _ in range(int(input())):
    n=int(input())
    for i in range(10):
        if n%10==0:
            print(i)
            break
        else:
            n*=2
    else:
        print(-1)
