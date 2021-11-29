# 유기농 배추

from collections import deque

t = int(input())
n_list, m_list, k_list = [], [], []
xy_list = [ [] for _ in range(t) ]

for idx in range(t):
    
    n, m, k = map(int, input().split())
    n_list.append(n)
    m_list.append(m)
    k_list.append(k)
    
    for _ in range(k):
        xy_list[idx].append(tuple(map(int, input().split())))
        

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
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
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = 2
                q.append((nx, ny))
    

result_list = []
for i in range(t):
    maps = [ [0] * (m_list[i]+1) for _ in range(n_list[i]+1) ] 
    for xy in xy_list[i]:
        x, y = xy
        maps[x][y] = 1
    
    cnt = 0
    for j in range(n_list[i]):
        for k in range(m_list[i]):
            if maps[j][k] == 1:
                bfs(j, k)
                cnt += 1
                
    result_list.append(cnt)
    
for rst in result_list:
    print(rst)