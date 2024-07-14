# Digit Sum Parities
def sm (x):
    x = str(x)
    s = 0
    for i in x:
        s += int(i)
    return s
    
for _ in range(int(input())):
    n = int(input())
    if sm(n)%2 == sm(n+1)%2: # if the parity of n and n+1 is same then the answer is n+2
        print(n+2)
    else:    # otherwise anser is n+1
        print(n+1)
