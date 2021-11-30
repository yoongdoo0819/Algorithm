# 숨바꼭질

from collections import deque

n, m = map(int, input().split())
maps = [ [] for _ in range(n+1) ]

for _ in range(m):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)
    
    
visited = [-1] * (n+1)
visited[1] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        
        for next in maps[v]:
            if visited[next] == -1:
                visited[next] = visited[v] + 1
                q.append(next)
                

bfs(1)
max_val = max(visited)
for i in range(1, n+1):
    if visited[i] == max_val:
        print(i, visited[i], visited.count(max_val))
        break