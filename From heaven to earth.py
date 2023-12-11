# From heaven to earth
import math
for _ in range(int(input())):
    n,s,e = map(int,input().split())
    sn = math.sqrt(2) * n
    en = 2 * n  
    if sn/s < en/e:
        print('Stairs')
    else:
        print('Elevator')
