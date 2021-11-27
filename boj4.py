# 효율적인 해킹
from collections import deque

n, m = map(int, input().split())
maps = [ [] for _ in range(n+1) ]
result = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    maps[y].append(x)


def bfs(start, visited, num_of_hacked):
    
    visited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        
        for next in maps[v]:
            if not visited[next]:
                visited[next] = True
                num_of_hacked += 1
                q.append(next)
                
    result[start] = num_of_hacked
    
for idx in range(1, n+1):
    visited = [False] * (n+1)
    bfs(idx, visited, 0)
    
max = max(result)
for idx in range(len(result)):
    if max == result[idx]:
        print(idx, end = ' ')
    
