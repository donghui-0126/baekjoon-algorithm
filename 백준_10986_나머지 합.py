import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
dp = [0] * (M)

S = 0
cnt= 0

for i in range(N):
    S += num[i]

    if S%M == 0:
        cnt +=1
    
    dp[S%M] += 1

anwser = cnt*(cnt-1)/2 + cnt

for j in range(1, M):
    if dp[j]!= 0:
        anwser += dp[j]*(dp[j]-1)/2


print(int(anwser))