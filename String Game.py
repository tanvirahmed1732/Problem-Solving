# String Game
for _ in range(int(input())):
    n = int(input())
    st = input()
    b = True
    for i in st:
        if(st.count(i)%2 != 0):
            b = False
            break
    if b:
        print('YES')
    else:
        print('NO')
