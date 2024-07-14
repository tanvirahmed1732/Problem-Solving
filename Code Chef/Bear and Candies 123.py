# cook your dish here
for i in range(int(input())):
    a, b = map(int,input().split())
    mx = a if a>b else b
    # print(mx)
    bob = 0
    lim = 0
    # print(a,b)
    for i in range(1,mx+2):
        # print(i)
        if(i%2 == 1):
            if(i>a):
                print("Bob")
                break
            else:
                lim = lim + i
                a = a - i
                # print("check")
        else:
            if(i>b):
                print("Limak")
                break
            else:
                 bob = bob + i
                 b = b - i
                #  print('Check2')
           
        # if(a<lim):
        #     print("Bob")
        #     break
        # elif(b<bob):
        #     print("Limak")
        #     break