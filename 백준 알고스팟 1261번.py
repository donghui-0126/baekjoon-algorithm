import sys
import heapq
sys.setrecursionlimit(10000000)
input= sys.stdin.readline

 #가로n, 세로m
n, m = map(int, input().split())

#미로 a
a = []
 
for i in range(m):
    a.append(input().strip("\n"))

 #거리를 나타내는 dist
dp = [[False]*n for _ in range(m)]
dp[0][0] = 0

#heap에 튜플형태로 (깨는 벽 개수, y, x)
heap = []


def sol(y, x):
    heapq.heappush(heap, (0, 0, 0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dp[0][0] = True

    while heap:
        crash, y, x = heapq.heappop(heap)

        if x==n-1 and y==m-1:
            return crash
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<= nx < n) and (0 <= ny < m) and not dp[ny][nx]:
                dp[ny][nx] = True

                if a[ny][nx] == "0":
                    heapq.heappush(heap, (crash, ny, nx))
                elif a[ny][nx] == "1":
                    heapq.heappush(heap, (crash+1, ny, nx))            


print(sol(0,0))


"""탐색할 때는 dx dy로 반복문 도는게 쉽다"""

"""최소힙을 사용하는 문제는 그냥 dp에 지나간지 안지나간지만 메모리제이션 해줘도 괜찮다."""