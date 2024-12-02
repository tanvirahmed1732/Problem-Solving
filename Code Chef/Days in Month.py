# https://www.codechef.com/problems/NW1
for _ in range(int(input())):
    w,s=map(str,input().split())
    w=int(w)
    lst=[w//7]*7
    dic={"mon":0, "tues":1, "wed":2, "thurs":3, "fri":4, "sat":5, "sun":6}
    temp=w%7
    t=dic[s]
    for i in range(temp):
        if t==7:
            t=0
        lst[t]+=1
        t+=1
    print(*lst)
