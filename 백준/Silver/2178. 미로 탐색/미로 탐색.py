import sys
from collections import deque

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        # 현재 노드에서 상하좌우에 있는 노드들 중 방문할 수 있는 곳이 있는지 확인하기 위한 for문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N) or not(0 <= ny < M):   # 새로 이동한 좌표 (nx, ny)가 그래프 범위 내인지 체킹, 아닐 경우 continue
                continue

            if graph[nx][ny] == 1:  # 현재 노드에서 상하좌우에 있는 노드들 중 갈 수 있는 곳이 있다면,
                graph[nx][ny] = graph[x][y] + 1   # 새로운 노드에 현재의 방문 횟수+1을 추가해주고
                que.append((nx,ny)) # 큐에도 추가해준다.
    
    return graph[N-1][M-1]




if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    graph=[]

    for _ in range(N):
        l = list(map(int, sys.stdin.readline().rstrip()))
        graph.append(l)
    
    ans = bfs(graph, 0, 0)
    print(ans)