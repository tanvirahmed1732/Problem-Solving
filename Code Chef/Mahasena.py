
# cook your dish here
#Mahasena
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i%2==0:
        c+=1
print("READY FOR BATTLE" if c>n/2 else "NOT READY")
