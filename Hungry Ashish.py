# Hungry Ashish
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if(x<y and x<z):
        print('NOTHING')
    elif(x>=y and x>=z):
        print('PIZZA')
    elif(x>=z):
        print('BURGER')
    else:
        print('PIZZA')
