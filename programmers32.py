from collections import deque

def bfs(x, y, n, computers, visited):
    q = deque()
    q.append(x)
    visited[x][y] = True
    
    while q:
        x = q.popleft()
        
        for i in range(n):
            if computers[x][i] == 1 and not visited[x][i]:
                visited[x][i] = True
                q.append(i)
                
            if computers[i][x] == 1 and not visited[i][x]:
                visited[i][x] = True
                q.append(i)
        
    return 1

def solution(n, computers):
    visited = [ [False] * n for _ in range(n) ]
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                visited[j][i] = True
                answer += bfs(i, j, n, computers, visited)
    
    return answer