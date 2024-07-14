# Alternating String
for _ in range(int(input())):
    n = int(input())
    s =  input()
    s0 = s.count('0')
    s1 = s.count('1')
    sm = min(s0,s1)
    if s0 == s1:
        print(s0*2)
    else:
        print(sm*2 + 1)
