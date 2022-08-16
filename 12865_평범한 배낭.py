#uncorrect code

#물건의 무게를 기준으로 dp를 만든게 아니라 물건을 기준으로 dp를 만들음. 
#그래서 논리에 오류가 발생함. 
# 사실상 dp는 사용하지 않은 것과 마찬가지 인듯...???

"""
import sys
input = sys.stdin.readline

N, max_weight = map(int, input().split())


#stuff[weight][value]
stuff = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] for _ in range(N)] for __ in range(N)]

for num in range(N):
    dp[num][num] = stuff[num]

current_max = 0

for h in range(N):
    for w in range(N):
        pre_weight, pre_value = dp[h][w-1][0], dp[h][w-1][1]
        now_weight, now_value = stuff[w][0], stuff[w][1]
        if pre_weight + now_weight <= max_weight:
            dp[h][w] = [pre_weight + now_weight, pre_value + now_value]

        else:
            dp[h][w] = dp[h][w-1]
    
    current_max = max(current_max, dp[h][w][1])


print(current_max)
"""

#Correct code
"""
무게 마다 담을 수 있는 최대의 가치를 저장하는 dp를 만들어서 푼다.
dp는 실행시간에 최적화가 된다!!!
"""
import sys
input = sys.stdin.readline

N, max_weight = map(int, input().split())
stuff = [[0, 0]]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

dp = [[0 for _ in range(max_weight + 1)] for __ in range(N+1)]


#물건을 하나씩 넣어본다.
for i in range(1, N+1):
    #put_weight = 내가 지금 가방에 넣을 무게
    for put_weight in range(1, max_weight+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        #현재 내가 가방에 담는 물건의 무게가 지금 가방에 담을 무게보다 무겁다면 전 dp값으로 갱신
        if put_weight < weight:
            dp[i][put_weight] = dp[i][put_weight-1]
        #현재 내가 가방에 넣을 물건의 무게가 지금 내가 가방에 담을 무게보다 가볍거나 같다면
        #(가방에 넣을 무게)와 (현재 집어 넣는 물건)의 무게의 차이에서 가장 큰 가치를 더한 값 
        #(dp[i-1][put_weight-weight] + value) 과 
        #원래 dp값으로 구해진 값(dp[i-1][put_weight])을 비교해서 큰값으로 갱신

        #이미 지나간 row에 대해서는 이미 가치 최대화가 되있음. 

        else:
            dp[i][put_weight] = max(dp[i-1][put_weight-weight] + value, dp[i-1][put_weight])

print(dp[-1][-1])