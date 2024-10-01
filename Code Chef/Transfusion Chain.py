# https://www.codechef.com/problems/TRANCHAIN?tab=statement
for _ in range(int(input())):
    n=int(input())
    lst=input()
    lst=lst.replace("AB","P")
    print(max(lst.count("A"),lst.count("B"))+lst.count("P")+lst.count("O"))
