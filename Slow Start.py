# cook your dish here
for i in range(int(input())):
    x,h = map(int, input().split())
    count, tp = 0 , 0
    temp = x/2
    while(h>0):
        if(tp<5):
            tp +=1
            h = h - temp
            # print(h)
            count +=1
            if(h<=0):
                break
        else:
            h = h - x
            count += 1
    print(count)
