# https://www.codechef.com/problems/TRUEDARE
for _ in range(int(input())):
    #taking the inputs
    tr=int(input())
    lsttr=list(map(int,input().split()))
    dr=int(input())
    lstdr=list(map(int,input().split()))
    ts=int(input())
    lstts=list(map(int,input().split()))
    ds=int(input())
    lstds=list(map(int,input().split()))
    
    b = True #flag to identify Ram wins or not
    for i in lstts: #if every truth task Shyam can ask is in the Ram can perform than it is okay
        if i in lsttr:
            continue
        else: #otherwise flag is False that means Ram can't win
            b = False
            break
    if b: #if Ram not lose yet.
        for i in lstds: #same checking for the dare tasks
            if i in lstdr:
                continue
            else:
                b=False
                break
    if b: #finally based on the identifier show the result
        print("yes")
    else:
        print("no")
