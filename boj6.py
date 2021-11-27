# 단지번호붙이기
from collections import deque

n = int(input())
maps = [ [0 for _ in range(n)] for _ in range(n) ]

for idx in range(n):
    s = input()
    for j in range(n):
        maps[idx][j] = s[j]
        
#for map in maps:
#    print(map)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 'X'
    ans = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if maps[nx][ny] == '1':
                ans += 1
                maps[nx][ny] = 'X'
                q.append((nx, ny))
            
    return ans

result = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            result.append(bfs(i, j))

print(len(result))
result.sort()
for rst in result:
    print(rst)           