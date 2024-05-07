# cook your dish here
for _ in range(int(input())):
    bt,bw = map(int, input().split())
    btlst = list(map(int,input().split()))
    bwlst = list(map(int,input().split()))
    btlst.sort(reverse=True)
    bwlst.sort(reverse=True)
    sm=0
    k,l=4,4
    x = -1
    if bt<4 or bw<4 or bt+bw<11:
        print(-1)
    else:
        for i in range(4):
            sm+=btlst[i]
            sm+=bwlst[i]
        for i in range(3):
            if k==bt:
                x = 0
                break
            elif l==bw:
                x = 1
                break
            if btlst[k]>bwlst[l]:
                sm+=btlst[k]
                k+=1
            else:
                sm+=bwlst[l]
                l+=1
        if x == -1:
            print(sm)
        elif x == 0:
            for i in range(11-k-l):
                sm+=bwlst[l]
                l+=1
            print(sm)
        elif x == 1:
            for i in range(11-k-l):
                sm+=btlst[k]
                k+=1
            print(sm)
