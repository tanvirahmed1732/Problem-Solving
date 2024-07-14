# Processing a string
for _ in range(int(input())):
    s = input()
    count = 0
    for i in s:
        if i in '123456789':
            count += int(i)
    print(count)
