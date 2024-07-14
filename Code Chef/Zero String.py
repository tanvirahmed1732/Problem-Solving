# cook your dish here
for _ in range(int(input())):
    n = int(input())
    str = input()
    c0 = str.count('0')
    c1 = str.count('1')
    if(c1>c0):
        print(c0+1)
    else:
        print(c1)
    
