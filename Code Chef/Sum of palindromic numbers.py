#https://www.codechef.com/problems/SPALNUM
# cook your dish here
def pal(x): #accepting string value
    if x==x[::-1]: #if the string match to its reverse
        return True #then it will be called palindrome
    else:
        return False

for _ in range(int(input())):
    ans = 0
    l,r=map(int,input().split())
    for i in range(l,r+1): #taking all number in that range
        temp=str(i) #converting the number to string to check palindrome or not
        if pal(temp): #the func return true that means the number is palindrome
            ans+=i #collect the sum of all palindrome number
    print(ans)
