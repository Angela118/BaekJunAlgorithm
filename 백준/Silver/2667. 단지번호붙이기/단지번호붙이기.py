import sys
from collections import deque


# 상 하 좌 우 (-1,0), (1,0), (0,-1), (0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y):
    global count
    graph[x][y] = 0     # 방문 했음을 표시
    count+=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=N:  # 움직인 좌표가 범위를 벗어날 경우
            continue
        if graph[nx][ny] == 1:  # 움직인 좌표에 집이 있는 경우, 다시 dfs 탐색
            dfs(nx, ny)
    
    



if __name__ == '__main__':
    N = int(sys.stdin.readline())

    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    houses=[]

    for x in range(N):
        for y in range(N):
            if graph[x][y] == 1:
                count=0
                dfs(x, y)
                houses.append(count)

    
    print(len(houses))
    houses.sort()
    for i in houses:
        print(i)