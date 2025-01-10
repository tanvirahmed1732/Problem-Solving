# cook your dish here
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    al=sorted(lst[:3])
    bb=sorted(lst[3:])
    alice=sum(al[1:])
    bob=sum(bb[1:])
    if(alice>bob):
        print("Alice")
    elif bob>alice:
        print("Bob")
    else:
        print("Tie")
