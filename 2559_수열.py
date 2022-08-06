import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int, input().split()))

S = 0 
s = [0]*N
for k in range(N):
    S += num[k]
    s[k] = S


if M == N:
    print(s[-1])
elif M==1:
    print(max(num))
else:
    m = 0
    for i in range(0, N-M+1):
        if i == 0:
            m = s[i+M-1]
        else:
            m = max(m, s[i+M-1]-s[i-1])

    print(m)

