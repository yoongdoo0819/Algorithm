# 토마토 (BOJ 7576) 
from collections import deque

m, n = map(int, input().split())
maps = [ [] for _ in range(n) ]
q = deque()

for i in range(n):
    maps[i] = list(map(int, input().split()))
    for j in range(m):
        if maps[i][j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(q):
    cnt = 0
    modification_check = 0
    
    while q:
        cnt += 1
        length_q = len(q)
        
        for _ in range(length_q):
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    modification_check += 1
        
    for map in maps:
        if 0 in map:
            return -1
    return cnt-1

print(bfs(q))