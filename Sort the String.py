# Sort the String
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in range(n-1):
        if s[i] == '1' and s[i+1] == '0':
            c += 1 
    print(c)
