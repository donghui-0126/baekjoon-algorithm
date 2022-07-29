import sys
sys.setrecursionlimit(10000)

L, W = map(int, input().split())

matrix = []

for _ in range(L):
    matrix.append(list(map(int, input().split())))

anwser = []

def DFS(x, y, L, W, mat, anwser):   
    """x, y는 시작 좌표 L,W는 2차원의 크기"""
    if (x== W-1 and y==L-1):
        anwser.append(-1)

    elif x==0 and y==0:    
        #시작좌표가 왼쪽위 꼭짓점인 경우
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x, y+1, L, W , mat, anwser)
    elif x==0 and y==L-1:
        #시작좌표가 왼쪽 아래 꼭짓점인 경우
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y-1][x] < mat[y][x]:
            DFS(x, y-1, L, W , mat, anwser)
    elif x==W-1 and y==0:
        #시작좌표가 오른쪽 위 꼭지점일 경우
        if mat[y][x-1] < mat[y][x]:
            DFS(x-1, y, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x, y+1, L, W , mat, anwser)
    elif x==0:
        #시작좌표가 꼭지점이 아니고 왼쪽벽인 경우
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y-1][x] < mat[y][x]:
            DFS(x, y-1, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x, y+1, L, W , mat, anwser)
    elif x==W-1:
        #시작좌표가 꼭지점이 아니고 오른쪽벽인 경우
        if mat[y][x-1] < mat[y][x]:
            DFS(x-1, y, L, W , mat, anwser)
        if mat[y-1][x] < mat[y][x]:
            DFS(x, y-1, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x, y+1, L, W , mat, anwser)
    elif y==0:
        #시작좌표가 꼭지점이 아니고 위쪽벽인 경우
        if mat[y][x-1] < mat[y][x]:
            DFS(x-1, y, L, W , mat, anwser)
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x, y+1, L, W , mat, anwser)
    elif y==L-1:
        #시작좌표가 꼭지점이 아니고 아래쪽벽인 경우
        if mat[y][x-1] < mat[y][x]:
            DFS(x-1, y, L, W , mat, anwser)
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y-1][x] < mat[y][x]:
            DFS(x, y-1, L, W , mat, anwser)
    else:
        #나머지
        if mat[y][x-1] < mat[y][x]:
            DFS(x-1, y, L, W , mat, anwser)
        if mat[y][x+1] < mat[y][x]:
            DFS(x+1, y, L, W , mat, anwser)
        if mat[y-1][x] < mat[y][x]:
            DFS(x, y-1, L, W , mat, anwser)
        if mat[y+1][x] < mat[y][x]:
            DFS(x,y+1, L, W, mat, anwser)
        
 

DFS(0, 0, L, W, matrix, anwser)
print(len(anwser))
