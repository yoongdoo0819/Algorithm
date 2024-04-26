# 공주님을 구해라

from collections import deque

n, m, t = map(int, input().split())
graph = []
visited = [ [0] * m for _ in range(n) ]
min_dist = 1e9

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            graph[i][j] = '*'
        elif graph[i][j] == 1:
            graph[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    global min_dist
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == '*':
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                min_dist = int(abs(n-nx-1) + abs(m-ny-1) + graph[nx][ny])

            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


bfs(0, 0)

if graph[n-1][m-1] == 0 and min_dist == 1e9: # 검도 없고, 공주가 벽에 둘러쌓여 있어서 구출하지 못한다면
    print("Fail")
elif graph[n-1][m-1] == 0 and min_dist != 1e9: # 검은 있으나, 공주가 벽에 둘러쌓여 있다면
    if min_dist > t: # 검을 주웠으나 시간 내에 구출할 수 없다면
        print("Fail")
    else: # 검을 주운 후 시간 내에 구출할 수 있다면
        print(min_dist)
elif graph[n-1][m-1] != 0 and min_dist != 1e9: # 검도 있고, 공주가 벽에 둘러쌓여 있지 않다면
    min_v = min(min_dist, graph[n-1][m-1])
    if min_v > t: # 시간 내에 구출할 수 없다면
        print("Fail")
    else:
        print(min_v)