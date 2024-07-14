# Coin Flip
for i in range(int(input())):
    for j in range(int(input())):
        i,n,g = map(int,input().split())
        if n%2 == 0:
            print(int(n/2))
        else:
            if i == 1:
                if g == 1:
                    print(n//2)
                else:
                    print((n//2) + 1)
            else:
                if g == 1:
                    print((n//2) + 1)
                else:
                    print(n//2)
