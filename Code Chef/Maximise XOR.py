# https://www.codechef.com/problems/XORMAX
for _ in range(int(input())):
    a=input()
    b=input()
    l=len(a) #finding the length of the given strings
    a1,b0=a.count("1"),b.count("0") #first counting the number of alternative value from those string.
    count=min(a1,b0) #check how many pair we can make with different value.
    count+=min(l-a1,l-b0) #first 1,0 pair then remaining 0,1 pair.
    ans="1"*count+"0"*(l-count) #assing the number of pair of different value amount of 1 and rest with zeros.
    print(ans) #it will be the largest number we can make after xor,
    #since in xor different value means 1, same value means 0.
