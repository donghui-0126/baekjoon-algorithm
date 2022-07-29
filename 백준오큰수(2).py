L = int(input())
num = list(map(int, input().split()))
answer = [-1] * L
stack = [0]

for i in range(1, L):
    while stack and num[i] > num[stack[-1]]:
        answer[stack.pop()] = num[i]
    stack.append(i)

print(*answer)