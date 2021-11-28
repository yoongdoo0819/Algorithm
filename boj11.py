# 인구 이동 (BOJ 16234)

from collections import deque

n, l, r = map(int, input().split())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    update_xy_list = []
    update_xy_list.append((x, y))
    sum = maps[x][y]
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            
            diff = abs(maps[x][y] - maps[nx][ny])
            if  diff >= l and diff <= r:
                visited[nx][ny] = True
                update_xy_list.append((nx, ny))
                sum += maps[nx][ny]
                cnt += 1
                
                q.append((nx, ny))
    
    avg = sum//cnt
    for xy in update_xy_list:
        x, y = xy
        maps[x][y] = avg         
            
days = 0
while True:
    migration_check = 0
    visited = [ [False] * n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)
                migration_check += 1
    
    if migration_check == n*n:
        break            
    days += 1
    
print(days)