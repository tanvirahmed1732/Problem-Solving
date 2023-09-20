# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in s:
        temp = s.count(i)
        if(temp%2 == 1):
            print("NO")
            break
    else: 
        print('YES')
