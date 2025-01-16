# https://www.codechef.com/problems/ARRSWAP
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a+=b #cobining both array to a.
    a.sort() #sort the combined array
    ans=float('inf') #initially assume that the answer is infinity to find the minimum answer
    for i in range(n+1):
        temp=a[i+n-1]-a[i] #in n portion check that is the require portion is not
        if temp<ans:
            ans=temp
    print(ans)
