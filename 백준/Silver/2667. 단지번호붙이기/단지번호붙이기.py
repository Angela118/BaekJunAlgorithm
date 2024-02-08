import sys
from collections import deque


# 상 하 좌 우 (-1,0), (1,0), (0,-1), (0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x,y):
    global count
    queue = deque()

    queue.append((x,y)) # 시작점(x, y)를 큐에 추가
    graph[x][y] = 0     # 방문 했음을 표시 (다시 방문하지 않기 위함. 중복방지)
    count+=1


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:  # 움직인 좌표가 범위를 벗어날 경우
                continue

            if graph[nx][ny] == 1:  # 움직인 좌표에 집이 있는 경우
                graph[nx][ny] = 0   # 방문 했음을 표시
                queue.append((nx, ny))
                count+=1
            
    return count



if __name__ == '__main__':
    N = int(sys.stdin.readline())

    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    houses=[]

    for x in range(N):      # 전체 그래프를 돌면서 집이 있는 곳만 dfs 실행
        for y in range(N):
            if graph[x][y] == 1:
                count=0
                houses.append(bfs(graph, x, y))

    
    print(len(houses))
    houses.sort()
    for i in houses:
        print(i)