# Football
for _ in range(int(input())):
    n = int(input())
    goal = list(map(int, input().split()))
    foul = list(map(int, input().split()))
    mx = []
    for i in range(n):
        if(goal[i]*20 - foul[i]*10)<1:
            mx.insert(i,0)
        else:
            mx.insert(i,(goal[i]*20 - foul[i]*10))
    print(max(mx))
