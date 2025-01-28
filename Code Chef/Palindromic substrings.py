# https://www.codechef.com/problems/STRPALIN
for _ in range(int(input())):
    a=input()
    b=input()
    for i in a:
        if i in b:
            print("Yes")
            break
    else:
        print("No")
