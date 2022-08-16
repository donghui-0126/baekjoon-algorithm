import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(H)]

#큐 사용
queue = deque()

#이동시키는 변수
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

#익은 토마토 위치 받기
y, x = 0, 0
for y in range(H):
    for x in range(W):
        if tomato[y][x] == 1:
            queue.append((y,x))
        

def BFS():
    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            ny, nx = now_y + dy[i], now_x+dx[i]
            if 0<=ny<H and 0<=nx<W and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[now_y][now_x] + 1
                queue.append((ny,nx))

BFS()

#답을 저장할 result 변수
res = 0
for li in tomato:
    for elem in li:
        if elem == 0:
            print(-1)
            exit(0)
    res = max(res, max(li))

print(res-1)