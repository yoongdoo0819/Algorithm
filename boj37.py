# 봄버맨 (BOJ 16918)

from collections import deque

maps = []
n, m, s = map(int, input().split())
cnt = 1
q = deque()

for i in range(n):
    maps.append(list(input()))
    for j in range(m):
        if maps[i][j] == 'O':
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    
    while q:
        x, y = q.popleft()
        maps[x][y] = '.'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            maps[nx][ny] = '.'


def all_bomb():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '.':
                maps[i][j] = 'O'


def insert_bomb_to_q():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'O':
                q.append((i, j))
                
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '.':
                maps[i][j] = 'O'


while cnt != s:
    
    all_bomb()    
    cnt += 1
    if cnt == s:
        break
    
    bfs()
    cnt += 1
    if cnt == s:
        break
    
    insert_bomb_to_q()
    

for map in maps:
    print("".join(map))
            
                
        