# 치즈

from collections import deque

n, m = map(int, input().split())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    

def del_outwall_bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 2
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == 0:
                q.append((nx, ny))
                maps[nx][ny] = 2

def check_del_outwall_bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    result = False
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= 0 or nx >= n-1 or ny <= 0 or ny >= m-1:
                result = True
                continue
            if visited[nx][ny] == True:
                continue
            if maps[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            
    return result

"""
visited = [ [False] * m for _ in range(n) ]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            target = 0
            result = check_del_outwall_bfs(i, j, target, visited)
            if result == True:
                del_outwall_bfs(i, j)
"""

def del_list_bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        melt = False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == True:
                continue
            if maps[nx][ny] == 2:
                melt = True
                
        if melt == True:
            maps[x][y] = 2
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] == True:
                    continue
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def sum_cheese():
    sum = 0
    for map in maps:
        sum += map.count(1)
    return sum
    
elapsed_hour = 0
prev_cnt = 0
while True:     
    visited = [ [False] * m for _ in range(n) ]
    cnt = sum_cheese()
    quit_cond = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                result = check_del_outwall_bfs(i, j, visited)
                if result == True:
                    del_outwall_bfs(i, j)

    visited = [ [False] * m for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                del_list_bfs(i, j, visited)
            else:
                quit_cond += 1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                maps[i][j] = 0
                
    if quit_cond == n*m:
        break
                    
    prev_cnt = cnt
    elapsed_hour += 1
    """
    print(elapsed_hour, prev_cnt)
    for map in maps:
        print(map)
    print("")
    """
print(elapsed_hour)
print(prev_cnt)

