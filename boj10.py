# 연구소 (BOJ 14502)

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = [ [] for _ in range(n) ]
q = deque()

for i in range(n):
    maps[i] = list(map(int, input().split()))
    for j in range(m):
        if maps[i][j] == 2:
            q.append((i, j))

for map in maps:
    print(map)
    
for i in range(len(maps)):
    for j in range(len(maps[i])):
        print(maps[i][j], end =' ')
    print("")
    
for element in q:
    print(element)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def calc(temp_maps):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_maps[i][j] == 0:
                cnt += 1
    return cnt

def bfs_check_safe_area(temp_maps):
    temp_q = deepcopy(q)
    
    while temp_q:
        x, y = temp_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if temp_maps[nx][ny] == 0:
                temp_maps[nx][ny] = 2
                temp_q.append((nx, ny))
                

    return calc(temp_maps)

#max_val = 0
def construct_wall(count, max_val):
    #global max_val
    
    if count == 3:
        temp_maps = deepcopy(maps)
                
        new_val = bfs_check_safe_area(temp_maps)
        max_val = max(max_val, new_val)
        
    else:
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    count += 1
                    
                    new_val = construct_wall(count, max_val)
                    max_val = max(max_val, new_val)
                    maps[i][j] = 0
                    count -= 1
    
    return max_val
    
max_val = construct_wall(0, 0)
print(max_val)