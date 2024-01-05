# Chef and Card Game
def sd(x):
    s = 0
    for i in str(x):
        s += int(i)
    return s 
for _ in range(int(input())):
    n = int(input())
    a,b=0,0
    for i in range(n):
        c,d = map(int, input().split())
        if sd(c) > sd(d):
            a+=1 
        elif sd(c) == sd(d):
            a += 1 
            b += 1 
        else:
            b += 1
    print('0 ' + str(a) if a > b else '1 ' + str(b) if b > a else '2 ' + str(a))
