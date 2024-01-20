# Large Square
import math
for _ in range(int(input())):
    n,x = map(int, input().split())
    b = int(math.sqrt(n))
    print(x*b)
