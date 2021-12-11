# 네트워크

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, n, computers, visited):
    
    q = deque()
    q.append(y)
    visited[y] = 1
    
    while q:
        x = q.popleft()
        
        for idx in range(1, n-y):
            if computers[x][y+idx] == 1 and visited[y+idx] == -1:
                visited[y+idx] = 1
                q.append(y+idx)
            
    return 1

def solution(n, computers):
    
    visited = [-1] * n 
    cnt = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == -1:
                cnt += bfs(i, j, n, computers, visited)
                
    return cnt