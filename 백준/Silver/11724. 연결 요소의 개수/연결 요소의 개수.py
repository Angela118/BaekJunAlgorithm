import sys

sys.setrecursionlimit(10000)


def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=" ")
    for neighbor in graph[v]:
        if visited[neighbor]==False:
            dfs(graph, neighbor, visited)
        


    

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] * (N+1) for _ in range(N+1)]    # 1~N

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # print(graph)

    visited = [False] * (N+1)
    count=0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(graph, i, visited)
            count+=1

    print(count)