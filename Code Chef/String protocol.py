# cook your dish here
for _ in  range(int(input())):
    n = int(input())
    s = input()
    i = 0
    count = 0
    while(i<n):
        if(i<n-1 and s[i] == s[i+1]):
            count +=1 
            i+=2
        else:
            count += 1 
            i += 1 
    print(count)
