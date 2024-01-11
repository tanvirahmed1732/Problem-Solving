# Ciel and A-B Problem
a,b = map(int, input().split())
c = a - b 
d = str(c)
if(int(d[0])<6 or int(d[0])>6):
    e = '6' + d[1:]
else:
    e = '5' + d[1:]
print(e)
