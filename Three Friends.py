# cook your dish here
for _ in range(int(input())):
    x,y,z = map(int, input().split())
    if x + y == z or y + z == x or x + z == y: #here is the condition. if the summation of all difference is zero 
      #then the a b c is possible. we need to check if x + y + z == 0 or not. for the first case 
      #there is 1-2+1 which is zero that's why we get a b c. similarly the second case is not satisfied.
        print('yes')
    else:
        print('no')
