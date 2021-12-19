# 벽 부수고 이동하기 (BOJ 2206)

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = [ [] for _ in range(2) ]

for i in range(n):
    maps[0].append(list(map(int, input())))
    for j in range(m):
        if maps[0][i][j] == 1:
            maps[0][i][j] = -1
    
maps[1] = deepcopy(maps[0])
    
visited = [ [ [False] * m for _ in range(n) ] for _ in range(2) ]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(k, x, y):
    q = deque()
    q.append((k, x, y))
    visited[k][x][y] = True
    visited[k+1][x][y] = True
    maps[k][x][y] = 1
    maps[k+1][x][y] = 1
         
    while q:
        k, x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            return maps[k][x][y]        
    
        if k == 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == 0 and not visited[k][nx][ny]:
                    visited[k][nx][ny] = True
                    maps[k][nx][ny] = maps[k][x][y] + 1            
                    q.append((k, nx, ny))
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == -1 and not visited[k][nx][ny]:
                    visited[k+1][nx][ny] = True
                    maps[k+1][nx][ny] = maps[k][x][y] + 1
                    q.append((k+1, nx, ny))
                    
        if k == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[k][nx][ny] == 0 and not visited[k][nx][ny]:
                    visited[k][nx][ny] = True
                    maps[k][nx][ny] = maps[k][x][y] + 1            
                    q.append((k, nx, ny))
                
    return -1

print(bfs(0, 0, 0))

"""

위 코드처럼 while 문을 반복하면서 q에서 가장 먼저 k에 대해 n-1, m-1 좌표를 도달했을 때 결과를 출력

아래 코드는 q가 빌때까지 while문을 모두 반복한 뒤, 결과를 출력

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [ [] for _ in range(2) ]

for i in range(n):
    graph[0].append(list(map(int, input())))
    for j in range(m):
        if graph[0][i][j] == 1:
            graph[0][i][j] = 'X'
            
graph[1] = deepcopy(graph[0])

r_k, r_x, r_y = 0, 0, 0
check = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(k, x, y):
    q = deque()
    q.append((k, x, y))
    graph[k][x][y] = 1
    graph[k+1][x][y] = 1
    global r_k, r_x, r_y, check
    while q:
        k, x, y = q.popleft()
        
        if k < 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[k][nx][ny] == 0:
                    graph[k][nx][ny] = graph[k][x][y] + 1
                    q.append((k, nx, ny))
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[k][nx][ny] == 0 or graph[k][nx][ny] == 'X':
                    graph[k+1][nx][ny] = graph[k][x][y] + 1
                    q.append((k+1, nx, ny))
                    
        if k == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[k][nx][ny] == 0:
                    graph[k][nx][ny] = graph[k][x][y] + 1
                    q.append((k, nx, ny))
    return -1    
            
bfs(0, 0, 0)
if graph[0][n-1][m-1] == 0 and graph[1][n-1][m-1] == 0:
    print(-1)
else:
    if graph[0][n-1][m-1] == 0:
        print(graph[1][n-1][m-1])
    elif graph[1][n-1][m-1] == 0:   # 이 조건이 없이 151 line 조건만 존재한다면 실패함.
        print(graph[0][n-1][m-1])   # k가 0인데 n-1, m-1에 도달할 수 있으나, k가 1인데 n-1, m-1에 도달할 수 없는 경우가 존재하는듯. 그러한 예시는?? 아래 152 line에서 설명함
    elif graph[0][n-1][m-1] > 0 and graph[1][n-1][m-1] > 0:
        print(min(graph[0][n-1][m-1], graph[1][n-1][m-1]))
        
# 위의 if-else문을 아래와 같이 변경하면 통과함.
if graph[0][n-1][m-1] == 0 and graph[1][n-1][m-1] == 0:
    print(-1)
else:
    if graph[0][n-1][m-1] > 0 and graph[1][n-1][m-1] == 0: # 벽을 부수지 않은 맵에서는 도달하였으나, 벽을 부순 맵에서는 도달하지 못한 경우라면,
        print(graph[0][n-1][m-1])                          # 벽을 부수지 않은 맵에서 n-1, m-1에 인접한 좌표에서 n-1, m-1로 도달한다면 graph[0][n-1][m-1]의 값은 0보다 커짐.
                                                           # 그러나, 벽을 부숴서 이동하는 맵에서는, 이미 graph[0][n-1][m-1]의 값이 0보다 크며 벽이 아니므로, graph[1][n-1][m-1]의 값은 업데이트되지 않음.
    else:
        print(graph[1][n-1][m-1])

"""