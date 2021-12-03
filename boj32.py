# 불! (BOJ 4179)

from collections import deque

n, m = map(int, input().split())
maps = []
j_q = deque()
fire_q = deque()

for i in range(n):
    maps.append(list(input()))
    for j in range(m):
        if maps[i][j] == 'J':
            j_q.append((i, j))
        elif maps[i][j] == 'F':
            fire_q.append((i, j))
    
h = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global h
    visited = [ [False] * m for _ in range(n) ]
        
    while j_q:
        
        for _ in range(len(fire_q)):
            x, y = fire_q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[nx][ny] == '.' or maps[nx][ny] == 'J':
                    maps[nx][ny] = 'F'
                    fire_q.append((nx, ny))
                    
        for _ in range(len(j_q)):
            x, y = j_q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    print(h+1)
                    exit()
                    
                if maps[nx][ny] == '.' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    j_q.append((nx, ny))
        h += 1
        
    return 'IMPOSSIBLE'

print(bfs())

"""
아래 코드는 시간 초과 발생

def j_bfs():
    visited = [ [False] * m for _ in range(n) ]
    
    for _ in range(len(j_q)):
        x, y = j_q.popleft()
        
        if maps[x][y] == 'F' or maps[x][y] == '#':
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print(h+1)
                exit()
                
            if maps[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                j_q.append((nx, ny))
            
    if j_q:
        return True
    else:
        return False 
    
def f_bfs():
    
    for _ in range(len(fire_q)):
        x, y = fire_q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == '.' or maps[nx][ny] == 'J':
                maps[nx][ny] = 'F'
                fire_q.append((nx, ny))
            
            
while True:
    if j_bfs() == True:
        
        h += 1
        f_bfs()
        print("=====")
        for map in maps:
            print(map)
        print("=====")
    else:
        print('IMPOSSIBLE')
        exit()
"""