import sys
sys.setrecursionlimit(10000)

# 상 하 좌 우 (-1,0), (1,0), (0,-1), (0,1)
da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]


def dfs(a, b):
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]

        if na<0 or na>=N or nb<0 or nb>=M:
            continue
        # if (0 <= na < N) and (0 <= nb < M):  # 움직인 좌표가 범위를 벗어날 경우
        if graph[na][nb] == 1:  # 움직인 좌표에 집이 있는 경우, 다시 dfs 탐색
            graph[na][nb] = -1
            dfs(na, nb)
    
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())    # N X M 행열

        graph = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            graph[Y][X] = 1 # X가 가로 길이(행), Y가 세로 길이 (열)

        count=0
        for i in range(N):      # 전체 그래프를 돌면서 집이 있는 곳만 dfs 실행
            for j in range(M):
                if graph[i][j] == 1:
                    count+=1
                    dfs(i, j)
                    

        print(count)