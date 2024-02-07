import sys
from collections import deque


N, M, V = map(int, sys.stdin.readline().split())

# 0으로 채워진 (N+1) X (N+1) 행렬을 만든다.
# 0번째 행과 열은 사용하지 않는다. 1~N까지의 행과 열만 사용.
graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

# 방문 체크 리스트
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)



def dfs(V):
        visited_dfs[V] = True   # 현재 노드를 방문 처리
        print(V, end=" ")   # 방문한 노드 출력

        # 현재 노드와 연결된 아직 방문한 적 없는 노드들을 재귀적으로 방문
        for i in range(1, N+1):   
            if not visited_dfs[i] and graph[V][i]==1:
                dfs(i)


def bfs(V):
    q = deque([V])  # Queue 사용을 위한 deque
    visited_bfs[V] = True   # 현재 노드를 방문 처리

    while q:    # 큐가 빌 때 까지 돈다
        V = q.popleft() # 큐에 있는 첫 번째 값을 꺼낸다.
        print(V, end=" ")   # 출력
        
        # 현재 노드와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(1, N+1):   
            if not visited_bfs[i] and graph[V][i]==1:
                q.append(i)
                visited_bfs[i] = True




dfs(V)
print()
bfs(V)