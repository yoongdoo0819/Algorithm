# 지뢰 찾기 (BOJ 4396)

from collections import deque

q = deque()
n = int(input())
maps1 = []
for i in range(n):
    maps1.append(list(input()))
    for j in range(n):
        if maps1[i][j] == '*':
            q.append((i, j))
            
maps2 = []
for _ in range(n):
    maps2.append(list(input()))
    
    
result = [ [0] * n for _ in range(n) ]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
bomb = False

for i in range(n):
    for j in range(n):
        if maps1[i][j] == '.' and maps2[i][j] == '.':
            result[i][j] = '.'
        
        elif maps1[i][j] == '.' and maps2[i][j] == 'x':
            x, y = i, j
            cnt = 0
            for idx in range(8):
                nx = x + dx[idx]
                ny = y + dy[idx]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if maps1[nx][ny] == '*':
                    cnt += 1
            result[i][j] = str(cnt)
            
        elif maps1[i][j] == '*' and maps2[i][j] == '.':
            result[i][j] = '.'
            
        elif maps1[i][j] == '*' and maps2[i][j] == 'x':
            bomb = True
            
if bomb == True:
    while q:
        x, y = q.popleft()
        result[x][y] = '*'
    
for row in result:
    print("".join(row))