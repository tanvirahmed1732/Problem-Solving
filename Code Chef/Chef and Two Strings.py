# cook your dish here
for i in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    lnt = len(s1)
    comp = 0
    compin = 0
    mxs1 = 0
    mxs2 = 0
    for i in range(lnt):
        if(s1[i] == s2[i] and s1[i]!= '?' and s2[i]!= '?'):
            comp += 1
        if(s1[i] != s2[i] and s1[i]!= '?' and s2[i]!= '?'):
            compin += 1
        if(s1[i] == '?'):
            mxs1 += 1 
        if(s2[i] == '?'):
            mxs2 += 1 
    print(compin, lnt - comp)
