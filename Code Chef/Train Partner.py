# Train Partner
for _ in range(int(input())):
    n = int(input())
    m = n%8
    d = n//8   #for further use
    if m == 7:
        print(str((d*8) + m + 1)+'SU') #printing the partenrs
    elif m == 0: # for 8th number sit
        print(str(((d-1)*8) + m + 7)+'SL') # printing the partenr for 8SU
    elif m == 1:
        print(str((d*8) + m + 3)+'LB')
    elif m == 2:
        print(str((d*8) + m + 3)+'MB')
    elif m == 3:
        print(str((d*8) + m + 3)+'UB')
    elif m == 4:
        print(str((d*8) + m -3)+'LB')
    elif m == 5:
        print(str((d*8) + m -3)+'MB')
    elif m == 6:
        print(str((d*8) + m -3)+'UB')
