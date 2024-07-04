# Rearranging digits to get a multiple of 5
for _ in range(int(input())):
    n=int(input())
    s=input()
    if '0' in s or '5' in s:
        print('Yes')
    else:
        print('No')
