# 빙산 (BOJ 2573)

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = []
q = deque()
h = 0

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] >= 1:
            q.append((i, j))

if not q:
    print(0)
    exit()
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def num_of_groups_bfs(x, y, temp_maps, visited):
    get_groups_q = deque()
    get_groups_q.append((x, y))
    temp_maps[x][y] = 0
    visited[x][y] = True
    
    while get_groups_q:
        x, y = get_groups_q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if temp_maps[nx][ny] != 0 and visited[nx][ny] == False:
                temp_maps[nx][ny] = 0
                visited[nx][ny] = True
                get_groups_q.append((nx, ny))
    return 1

def bfs():
    update_q = deque()
    
    for _ in range(len(q)):
        x, y = q.popleft()
        cnt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == 0:
                cnt += 1
                
        update_q.append((x, y, cnt))
        
    while update_q:
        x, y, cnt = update_q.popleft()
        
        if maps[x][y] - cnt <= 0:
            maps[x][y] = 0
        else:
            maps[x][y] -= cnt
            q.append((x, y))
        

def get_num_of_groups():
    visited = [ [False] * m for _ in range(n) ]
    num_of_groups = 0
    temp_maps = deepcopy(maps)
    
    for i in range(n):
        for j in range(m):
            if temp_maps[i][j] != 0:
                num_of_groups += num_of_groups_bfs(i, j, temp_maps, visited)
                
    if num_of_groups >= 2:
        print(h)
        exit()
    elif num_of_groups == 1:
        return False
    elif num_of_groups == 0:
        print(0)
        exit()

while True:
    
    if not get_num_of_groups():
        bfs()
        h += 1