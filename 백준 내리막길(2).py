import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
import sys
sys.setrecursionlimit(10000)

L, W = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(L)]
dp = [[-1]*W for i in range(L)]

def move(y, x):

    if x== W-1 and y==L-1: return 1
    if dp[y][x]!=-1: return dp[y][x] 

    count = 0
    if x>0 and matrix[y][x-1] < matrix[y][x]: 
        count += move(y, x-1)
    if x<W-1 and matrix[y][x+1] < matrix[y][x]:
        count += move(y, x+1)
    if y>0 and matrix[y-1][x] < matrix[y][x]: 
        count += move(y-1, x)
    if y<L-1 and matrix[y+1][x] < matrix[y][x]: 
        count += move(y+1, x)
    dp[y][x] = count
    return dp[y][x]

move(0, 0)
