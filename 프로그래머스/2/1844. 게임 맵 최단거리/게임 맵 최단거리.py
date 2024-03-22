from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]    
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0, 0, 1)])  # (x, y, cnt)
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x==n-1 and y==m-1:   # 프로그램 종료
            return cnt
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx, ny, cnt+1))
            
    
    
    return -1