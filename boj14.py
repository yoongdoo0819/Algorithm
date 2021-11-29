# 공주님을 구해라

from collections import deque
from copy import deepcopy

n, m, t = map(int, input().split())
maps = []
sword_xy = []
min_xy = 1e9

for _ in range(n):
    maps.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            maps[i][j] = 'X'
        elif maps[i][j] == 2:
            maps[i][j] = 'S'

temp_maps = deepcopy(maps)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_sword_bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [ [False] * m for _ in range(n) ]
    visited[x][y] = True
    if temp_maps[x][y] == 'S':
        temp_maps[x][y] = 0
        sword_xy.append((temp_maps[x][y], x, y))
                    
    while q:
        x, y = q.popleft()
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: 
                continue
            
            if temp_maps[nx][ny] == 'X':
                continue
            
            if visited[nx][ny] == True:
                continue
            
            if temp_maps[nx][ny] == 0:
                visited[nx][ny] = True
                temp_maps[nx][ny] = temp_maps[x][y] + 1
                q.append((nx, ny))
                
            elif temp_maps[nx][ny] == 'S':
                visited[nx][ny] = True
            
                temp_maps[nx][ny] = temp_maps[x][y] + 1
                
                sword_xy.append((temp_maps[nx][ny], nx, ny))
                q.append((nx, ny))    
    
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [ [False] * m for _ in range(n) ]
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            if maps[nx][ny] == 0:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
            
    
find_sword_bfs(0, 0)
for xy in sword_xy:
    dist_to_sword, x, y = xy
    total_dist = dist_to_sword + abs(n-1-x) + abs(m-1-y)
    min_xy = min(min_xy, total_dist)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            maps[i][j] = 0

bfs(0, 0)

#min_val = min(min_xy, maps[n-1][m-1])
if maps[n-1][m-1] == 0 and min_xy == 1e9: # 검도 없고, 공주가 벽에 둘러쌓여 있어서 구출하지 못한다면
    print('Fail')
elif maps[n-1][m-1] == 0 and min_xy != 1e9: # 검은 있으나, 공주가 벽에 둘러쌓여 있다면
    if min_xy > t: # 검을 주웠으나 시간 내에 구출할 수 없다면
        print("Fail")
    else:   # 검을 주운 후 시간 내에 구출할 수 있다면
        print(min_xy)
elif maps[n-1][m-1] != 0 and min_xy != 1e9: # 검도 있고, 공주가 벽에 둘러쌓여 있지 않다면
    min_val = min(min_xy, maps[n-1][m-1])
    if min_val > t: # 시간 내에 구출할 수 없다면
        print("Fail")
    else:
        print(min_val)
