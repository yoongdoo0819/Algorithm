# 벽 부수고 이동하기 (BOJ 2206)

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = [ [] for _ in range(2) ]

for i in range(n):
    maps[0].append(list(map(int, input())))
    for j in range(m):
        if maps[0][i][j] == 1:
            maps[0][i][j] = -1
    
maps[1] = deepcopy(maps[0])
    
visited = [ [ [False] * m for _ in range(n) ] for _ in range(2) ]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(k, x, y):
    q = deque()
    q.append((k, x, y))
    visited[k][x][y] = True
    visited[k+1][x][y] = True
    maps[k][x][y] = 1
    maps[k+1][x][y] = 1
         
    while q:
        k, x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            return maps[k][x][y]        
    
        if k == 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == 0 and not visited[k][nx][ny]:
                    visited[k][nx][ny] = True
                    maps[k][nx][ny] = maps[k][x][y] + 1            
                    q.append((k, nx, ny))
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == -1 and not visited[k][nx][ny]:
                    visited[k+1][nx][ny] = True
                    maps[k+1][nx][ny] = maps[k][x][y] + 1
                    q.append((k+1, nx, ny))
                    
        if k == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == 0 and not visited[k][nx][ny]:
                    visited[k][nx][ny] = True
                    maps[k][nx][ny] = maps[k][x][y] + 1            
                    q.append((k, nx, ny))
                
    return -1

print(bfs(0, 0, 0))