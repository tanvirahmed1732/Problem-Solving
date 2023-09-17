# cook your dish here
for i in range(int(input())):
    n, b = map(int, input().split())
    mx = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        if(p<=b):
            if(mx<(w*h)):
                mx = w*h
    if(mx == 0):
        print("no tablet")
    else:
        print(mx)
