# Covid and Theatre Tickets
import math
for _ in range(int(input())):
    n,m = map(int, input().split())
    print(math.ceil(m/2)*math.ceil(n/2)) #piece of cake
