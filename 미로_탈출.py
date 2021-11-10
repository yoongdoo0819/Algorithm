from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            # 첫 번째 (0,0) 위치가 다시 방문되어도 값이 1로 유지되도록 하기 위해 
            # (본 문제에서는 사실상 제거해도 무방)
            if nx == 0 and ny == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0, 0))
print(graph)