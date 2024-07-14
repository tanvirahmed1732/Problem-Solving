# Bi_lindrome!
for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in s:
        if s.count(i)>1: # if there is any double character available then the anser is n-2
            print(n-2)
            break
    else:
        print(-1)
