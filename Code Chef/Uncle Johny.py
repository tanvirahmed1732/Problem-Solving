# Uncle Johny
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    k = int(input())
    temp = lst[k-1] # storing the uncle jhony's length to find in sorted array
    lst.sort() #sort the array 
    print(lst.index(temp)+1) #printing the after sorting position.
