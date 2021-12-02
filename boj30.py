# 모양 만들기

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = []
group_num = 2
group_list = {}

for i in range(n):
    maps.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [False] * m for _ in range(n) ]
    
def classification(x, y):
    global group_num
    q = deque()
    q.append((x, y))
    cnt = 1
    visited[x][y] = True
    maps[x][y] = group_num
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                maps[nx][ny] = group_num
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    
    return cnt

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            cnt = classification(i, j)
            group_list[group_num] = cnt
            group_num += 1
            
max_val = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            cnt = 1
            x, y = i, j
            group_num_set = set()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
    
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[nx][ny] == 0:
                    continue
            
                group_num_set.add(maps[nx][ny])
                
            for group_num in group_num_set:
                cnt += group_list[group_num]
            
        max_val = max(max_val, cnt)
            
print(max_val)
