import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
number = list(map(int, input().split()))
dp = [[-1] * (n) for _ in range(n)]
m = int(input())


def sol(h, t):
    if h==t:
        return 1
    elif h+1==t:
        if number[h-1] != number[t-1]:
            return 0
        else:
            return 1
    
    if dp[h-1][t-1] != -1:
        return dp[h-1][t-1]
    
    if number[h-1] != number[t-1]:
        dp[h-1][t-1]=0
    else:
        dp[h-1][t-1] = sol(h+1,t-1)

    return dp[h-1][t-1]

for _ in range(m):
    h, t = map(int, input().split(" "))
    print(sol(h,t))