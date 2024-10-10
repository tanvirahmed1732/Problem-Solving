# cook your dish here
for _ in range (int(input())):
    n=int(input())
    if n<=10:
        print("Lower Double")
    elif n<=15:
        print("Lower Single")
    elif n<=25:
        print("Upper Double")
    else:
        print("Upper Single")
