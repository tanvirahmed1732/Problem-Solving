# https://www.codechef.com/problems/BRACKETS
for _ in range(int(input())):
    s=input()
    c=0
    mc=0
    for i in s:
        if i == "(":
            c+=1
        else:
            c-=1
        mc=max(mc,c)
    print("("*mc+")"*mc)
