# Magician versus Chef
for _ in range(int(input())):
    n,x,s = map(int, input().split())
    for i in range(s):
        a,b = map(int, input().split())
        if x == a: # if the coin in the swap box then we replace the x(pointer) with another box.
            x = b
        elif x == b:
            x = a
    print(x)
