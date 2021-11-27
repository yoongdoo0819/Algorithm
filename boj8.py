# 토마토 (BOJ 7569)

from collections import deque

m, n, h = map(int, input().split())
maps = [ [ [0] for _ in range(n) ] for _ in range(h) ]
q = deque()

for k in range(h):
    for i in range(n):
        maps[k][i] = list(map(int, input().split()))
        for j in range(m):
            if maps[k][i][j] == 1:
                q.append((k, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dk = [-1, 1]

"""
for k in range(h):
    for i in range(n):
        print(k, i, maps[k][i])
"""

def bfs(q):
    cnt = 0
    
    while q:
        cnt += 1
        length_q = len(q)
        
        for _ in range(length_q):
            k, x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[k][nx][ny] == 0:
                    maps[k][nx][ny] = maps[k][x][y] + 1
                    q.append((k, nx, ny))
            
            for i in range(2):
                nk = k + dk[i]
                
                if nk < 0 or nk >= h:
                    continue
                
                if maps[nk][x][y] == 0:
                    maps[nk][x][y] = maps[k][x][y] + 1
                    q.append((nk, x, y))
            
    for map_k in maps:
        for map in map_k:
            if 0 in map:
                return -1
    return cnt-1

print("======")
for k in range(h):
    for i in range(n):
        print(k, i, maps[k][i])
print("======")

print(bfs(q))
