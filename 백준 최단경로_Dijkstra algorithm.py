import sys
import heapq


input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
#시작점 K
K = int(input())
#distance 테이블
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]


def Dijkstra(start):
    #시작지점 -> 시작시점의 거리, 가중치는 0
    dp[start] = 0
    heapq.heappush(heap, (0,start))

    while heap:
        #가중치, 현재노드 저장
        dist, now = heapq.heappop(heap)

        if dp[now] < dist:
            continue

        for w, next_node in graph[now]:
            next_wei = w + dist
            if dp[next_node] > next_wei:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei, next_node))
                

for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])

"""
최소힙을 이용한 코드작성이 원할하지 않아서 코드를 참고했는데 결국 시간초과가 계속 떠서 거의 다 참고 했다.
그런데 참고하면서 32번째 줄 next_wei를 w로 적어놔서 계속 틀려서 머리아팠는데 
저기를 고치니까 100%이해가 된 것 같다. 으갹갹 
"""