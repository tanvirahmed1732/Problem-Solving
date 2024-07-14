# Tanu and Head-bob
for _ in range(int(input())):
    n = int(input())
    ges = input()
    N = ges.count('N')
    Y = ges.count('Y')
    I = ges.count('I')
    if(I>0):
        print('INDIAN')
    elif(Y>0):
        print('NOT INDIAN')
    else:
        print('NOT SURE')
