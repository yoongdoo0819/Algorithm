# 경쟁적 전염

from collections import deque

n, m = map(int, input().split())

graph = []
virusData = []

for i in range(n):
    graph.append(list(map(int, input())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치 X, 위치 Y 삽입
            virusData.append((graph[i][j], 0, i, j))

virusData.sort()
queue = deque(virusData)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
            virus, sec, x, y = queue.popleft()
            
            if sec == target_s:
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    queue.append((virus, sec+1, nx, ny))

bfs()
print(graph)
print(graph[target_x-1][target_y-1])
            