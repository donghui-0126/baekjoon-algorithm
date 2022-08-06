import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int, input().split()))
question = [list(map(int, input().split())) for _ in range(M)]


s = []
S = 0

for i in range(N):
    S+=num[i]
    s.append(S)

for __ in range(M):
    print(s[question[__][1]-1] - s[question[__][0]-1] + num[question[__][0]-1])