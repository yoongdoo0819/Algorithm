# 늑대와 양

from collections import deque

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(input()))
    
#for map in maps:
#    print(map)

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
            
            if maps[nx][ny] == 'S':
                print(0)
                return False
            if maps[nx][ny] == '.':
                maps[nx][ny] = 'D'
    
    return True

def find_all_wolf_bfs():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'W':
                if bfs(i, j) == False:
                    return False 
    return True

if find_all_wolf_bfs() == True:
    print(1)
    for i in range(n):
        for j in range(m):
            print(maps[i][j], end='')
        print("")