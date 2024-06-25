# Palindrome Flipping
for _ in range(int(input())):
    n=int(input())
    s=input()
    if n%2==1:
        print("yes")
    else:
        print("yes" if s.count('1')%2==0 else 'no')
