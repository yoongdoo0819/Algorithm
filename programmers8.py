# 게임 맵 최단거리

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m, maps):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
        
def solution(maps):
    
    startX, startY = 0, 0
    n = len(maps)
    m = len(maps[0])
    return bfs(startX, startY, n, m, maps)