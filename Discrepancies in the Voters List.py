# Discrepancies in the Voters List
n,o,p = map(int,input().split())
ns = []
for i in range(n+o+p):
    ns.insert(i,int(input()))
ns.sort()
rs = []
j,c = 0,1
for i in range(len(ns)-1):
    if ns[i] == ns[i+1]:
        c += 1
    else:
        c = 1
    if c > 1:
        rs.insert(j,ns[i])
        j += 1
        c = 0
print(len(rs))
for i in range(len(rs)):
    print(rs[i])
