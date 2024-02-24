# Problem (Shoes) - Solve the complete problem

t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    print(N if N<=M else 2*N-M)
