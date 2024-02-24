import sys


# 서 동 남 북 (-1,0), (1,0), (0,-1), (0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, total):
    global prob_ans

    if len(visited) == (N+1):   # 시작점을 포함하기 때문에 (N+1)
        prob_ans += total
        return
    
    for i in range(4):    # 동 서 남 북
        nx = x + dx[i]
        ny = y + dy[i]

        if [nx, ny] not in visited:     # 방문한 적 없으면
            visited.append([nx, ny])
            dfs(nx, ny, visited, total*prob_ewsn[i])
            visited.pop()



if __name__ == '__main__':
    N, e, w, s, n = map(int, sys.stdin.readline().split())
    prob_ewsn = [e, w, s, n]
    prob_ans=0

    dfs(0, 0, [[0,0]], 1)
    print(prob_ans * ((0.01)**N))   # %이기 때문에 0.01을 N번 곱해준다.

