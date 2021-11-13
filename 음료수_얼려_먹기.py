
# 음료수 얼려 먹기

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            dfs(nx, ny)
            
    return True

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            if dfs(i, j) == True:
                cnt += 1
                
print(cnt)