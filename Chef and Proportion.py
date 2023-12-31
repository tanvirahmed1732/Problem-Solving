# Chef and Proportion
s = list(map(int,input().split()))
s.sort()
#print(s)
if((s[1]/s[0]) == (s[3]/s[2])):
    print("Possible")
elif((s[2]/s[0] == (s[3]/s[1]))):
    print("Possible")
elif((s[3]/s[0] == (s[2]/s[1]))):
    print("Possible")
else:
    print("Impossible")
