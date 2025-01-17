# https://www.codechef.com/problems/GOODSET
for _ in range(int(input())):
    n=int(input())
    ar=[0]*n
    temp=1
    for i in range(n):
        ar[i]=temp
        temp+=2
    print(*ar) #the sum of two odd number is a even number.
    #but we don't have any even number in the ar.
