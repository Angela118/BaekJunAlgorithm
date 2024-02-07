import sys
from collections import deque


def dfs(graph, V, visited):
        visited[V] = True   # 현재 노드를 방문 처리
        print(V, end=" ")   # 방문한 노드 출력

        # 현재 노드와 연결된 아직 방문한 적 없는 노드들을 재귀적으로 방문
        for neighbor in graph[V]:   
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)


def bfs(graph, V, visited):
    q = deque([V])  # Queue 사용을 위한 deque
    visited[V] = True   # 현재 노드를 방문 처리

    while q:    # 큐가 빌 때 까지 돈다
        V = q.popleft() # 큐에 있는 첫 번째 값을 꺼낸다.
        print(V, end=" ")   # 출력
        
        # 현재 노드와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for neighbor in graph[V]:   
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True




N, M, V = map(int, sys.stdin.readline().split())

# 0으로 채워진 (N+1) X (N+1) 행렬을 만든다.
# 0번째 행과 열은 사용하지 않는다. 1~N까지의 행과 열만 사용.
graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# 방문 체크 리스트
visited = [False] * (N+1)

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)