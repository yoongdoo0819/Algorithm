# 치즈 (BOJ 2636)

"""
문제 조건에서 판의 가장자리는 치즈가 놓여있지 않음을 가정.
위와 같은 가정 때문에, 판의 가장자리에서부터 BFS 방식으로 (상,하,좌,우) 치즈가 놓여지지 않은 부분(공기; 숫자 0)을 탐색하면 
놓여진 치즈(숫자 1)들 중 가장자리에 놓인 치즈만 탐색할 수 있음 (놓여진 치즈들 내에 존재하는 공기는 접근하지 못하게하여) 

from collections import deque

N, M = map(int, input().split())
graphs = []

for _ in range(N):
    graphs.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
prev_cnt = 0
time = 0
def bfs(start_x, start_y, time):
    
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    xy_arr = []
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            visited[nx][ny] = True
            if graphs[nx][ny] == 0 :
                q.append((nx, ny))
            elif graphs[nx][ny] == 1 :
                xy_arr.append((nx, ny))
    
    prev_cnt = 0
    for graph in graphs:
        prev_cnt += graph.count(1)
        
    for x, y in xy_arr:
        graphs[x][y] = 0
        
    time += 1
    return time, prev_cnt
    
prev_cnt, curr_cnt = 0, 0
while True:
    prev_cnt = curr_cnt
    visited = [ [False] * M for _ in range(N) ]
    time, curr_cnt = bfs(0, 0, time)
    
    if curr_cnt == 0:
        break
    
print(time-1)
print(prev_cnt)
                
"""

"""
아래 코드는 판의 모든 공기(숫자 0)를 탐색. 
탐색하는 공기가 판의 가장자리로 나갈 수 있다면 치즈들 내에 존재하는 공기가 아니므로, 해당 공기 상,하,좌,우의 치즈는 녹이는 것

"""
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

