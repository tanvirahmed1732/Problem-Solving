# Movie Weekend
for _ in range(int(input())):
    n = int(input())
    lstl = list(map(int, input().split()))
    lstr = list(map(int, input().split()))
    temp = 0
    temp1 = 0
    ind = 0
    for i in range(n):
        if lstl[i]*lstr[i] > temp:
            temp = lstl[i]*lstr[i]
            temp1 = lstr[i]
            ind = i + 1
        elif lstl[i]*lstr[i] == temp:
            if lstr[i]>temp1:
                ind = i + 1
                temp1 = lstr[i]
    print(ind)
