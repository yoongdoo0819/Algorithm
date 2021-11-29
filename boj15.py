# 쉬운 최단거리

from collections import deque

n, m = map(int, input().split())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] == 1:
            maps[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == -1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
 
def start_bfs():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                bfs(i, j)
                return

start_bfs()
for i in range(n):
    for j in range(m):
        print(maps[i][j], end = ' ')   
    print("")