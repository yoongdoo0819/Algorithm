# 미로 탐색

from collections import deque

n, m = map(int, input().split())
maps = [ [ 0 for _ in range(m) ] for _ in range(n) ]

for idx in range(n):
    map = input()
    for j in range(len(map)):
        maps[idx][j] = int(map[j])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx, ny))
                
bfs(0, 0)
print(maps[n-1][m-1])

            
            
        
        
        