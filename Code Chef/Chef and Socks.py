a,b,c = map(int,input().split())
d=c-a
d=d//b
if d%2==0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')
