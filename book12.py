# 인구 이동

from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(n, l, r, graph)

migrationCnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    union = []
    union.append((x, y))
    
    sum = graph[x][y]
    count = 1
    
    tempBoard[x][y] = 1
    global migrationCnt
        
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or tempBoard[nx][ny] != 0:
                continue
            
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                
                sum += graph[nx][ny]
                count += 1
                tempBoard[nx][ny] = 1
                union.append((nx, ny))
                queue.append((nx, ny))
                print(x, y, nx, ny, graph[nx][ny], sum)
                
    if count > 1:
        for x, y in union:
            graph[x][y] = int(sum/count)
        print(graph)
        print(sum, count, int(sum/count))


while True:
    tempBoard = [ [0] * n for _ in range(n) ]
    index = 0
    for i in range(n):
        for j in range(n):
            if tempBoard[i][j] == 0:
                bfs(i, j)
                index += 1

    if index == n * n:
        break
    migrationCnt += 1
    
for col in graph:
    print(col)
    
print("answer ", migrationCnt)
