# 죽음의 비 (BOJ 22944)

from collections import deque

n, h, d = map(int, input().split())
graph = []

x, y = 0, 0
e_x, e_y = -1, -1

for i in range(n):
    graph.append(list(input()))
    for j in range(n):
        if graph[i][j] == 'S':
            x, y = i, j
            graph[i][j] = 0
        if graph[i][j] == 'E':
            e_x, e_y = i, j
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(initial_x, initial_y, initial_h, initial_d):
    q = deque()
    q.append((initial_x, initial_y, initial_h, initial_d))
    visited = [ [0] * n for _ in range(n) ]
    visited[initial_x][initial_y] = h
    
    while q:

        x, y, curr_h, curr_d = q.popleft()
        if curr_h <= 0:
            continue
        
        """
        아래 if문에 의해, 도착지점에 도달했음을 확인한 경우에
        return하지 않도록 코드를 짠 이유는,
        도착 지점에 도달하기 전에 체력이 1이고 도달하여 queue에 삽입할 때 체력이 0이 된다면, 
        추후 queue에서 꺼낼 때 32 line에서 체력이 0 이하로 꺼내지므로 다음 42 line if문 코드를 실행할 수가 없게 됨
        즉, 42 line 대신 53 line에서 도착 지점을 판별한다면 정답이 될 수 있는 이유는, 53 line을 실행하는 시점은 체력이 0보다 큰 경우이며 다음 지점이 도착 지점인 경우라면 도달할 수 있다는 것이므로 정답 처리가 됨. 
        
        if x == e_x and y == e_y:
            return True
        """
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] == 'E':
                graph[nx][ny] = graph[x][y] + 1
                return True

            next_h = curr_h
            next_d = curr_d
            
            if graph[nx][ny] == 'U':
                next_d = d
                
            if next_d == 0:
                next_h -= 1
            else:
                next_d -= 1
            
            """
            
            SU..
            .U..
            ....
            ...E
            
            위 그래프에서 두 번째 줄에 있는 우산까지 도달하는 경우,
            첫 번째 줄 우산을 거쳐가는 경우(오른쪽, 아래로 이동) 라면 체력이 고갈되지 않음.
            그러나 아래, 오른쪽으로 이동하여 우산에 도달하는 경우에는 죽음의 비를 맞아 체력이 깎이게 됨.
            따라서, 방문 처리를 단순히 queue에서 먼저 꺼내어 도달하는 방식으로만 처리하게 된다면,
            체력이 고갈되지 않는 방법으로 경로를 이어나갈 수 있음에도 불구하고, 체력이 고갈되는 상태로 경로를 이동할 수 있음. 
            
            따라서, 아래와 같이 코드를 작성하게 되면 안 됨.
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, next_h, next_d)) 
            """
            if visited[nx][ny] < next_h: 
                visited[nx][ny] = next_h
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, next_h, next_d)) 

    return False

if bfs(x, y, h, 0) == True:
    print(graph[e_x][e_y])
else:
    print(-1)