# https://www.codechef.com/problems/MAXSCORE7
for _ in range(int(input())):
    n=int(input())
    lst=input()
    print(min(lst.count('1'),lst.count('0')))
