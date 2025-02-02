# https://www.codechef.com/problems/SUBANAGR?tab=statement
n=int(input())
lst=[""]*n
ans=''
m=float('inf')
ind=0
for i in range(n): #this loop to collect all input
    lst[i]=input() #storing all given string
    if m>len(lst[i]): #find the smallest string to compare with others
        m=len(lst[i])
        ind=i
t=lst[ind] #store the smallest one
temp=''
for i in t:
    cnt=t.count(i) #take the freq of the characters
    if i not in temp: #if it is already not checked
        for j in lst: #take other string
            if cnt>=j.count(i): #and check that if there is same char available or not
                cnt=j.count(i) #if available take the smallest freq
        if cnt!=0: #if the char available in every string
            ans+=i*cnt
        temp+=i #string the char so that no duplicate checking
    # f=True
    # for j in lst:
    #     if i not in j:
    #         f=False
    #         break
    # if f:
    #     ans+=i
if len(ans) == 0: #if there is no matching char
    print("no such string")
else: #else print the sorted string for  lexicographically smaller
    print(''.join(sorted(ans)))
