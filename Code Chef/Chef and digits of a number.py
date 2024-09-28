# https://www.codechef.com/problems/LONGSEQ
for _ in range(int(input())):
    d=input()
    if d.count("0")==1 or d.count('1')==1:
        print("Yes")
    else:
        print("No")
