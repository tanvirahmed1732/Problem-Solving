# My First Geometry Problem
for i in range(int(input())):
    s=input()
    n = s.count('1')
    if n == 2:
        if s[0] == '1' and s[1] == '1':
            print(21)
        elif s[2] == '1' and s[3] == '1':
            print(21)
        else:
            print(121)
    else:
        print(11 if n ==1 else 231 if n == 3 else 1 if n == 0 else 441)
