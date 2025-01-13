# https://www.codechef.com/problems/CRDGAME3
import math
for _ in range(int(input())):
    c,r=map(int,input().split())
    c0=math.ceil(c/9) #the maximum one digit number is 9, so we can find minimum of
    r1=math.ceil(r/9)#digit needed by dividing by 9, and ceil to find the remaining number with 1 digit
    if c0==r1: #if equal number of digit, rick cheat and wins
        print(1,r1)
    elif c<r: #if chef has minimum number he wins
        print(0,c0)
    else: #else rick wins
        print(1,r1)
