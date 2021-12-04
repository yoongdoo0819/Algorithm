# 산책 (small) (BOJ 22868)

from collections import deque

n, m = map(int, input().split())
maps = [ [] for _ in range(n+1) ]

for _ in range(m):
    src, dst = map(int, input().split())
    maps[src].append(dst)
    maps[dst].append(src)

s, e = map(int, input().split())

for map in maps:
    map.sort()
    
def bfs(start, end, visited, path):
    q = deque()
    q.append(start)
    visited[start] = -1
    
    while q:
        v = q.popleft()
        if v == end:
            return
        
        for next in maps[v]:
            if not visited[next] and not next in path:
                visited[next] = v
                q.append(next)
        
        

visited = [False] * (n+1)
path = []
bfs(s, e, visited, path)
trace = e
while True:
    if visited[trace] == -1:
        break
    else:
        path.append(trace)
        trace = visited[trace]

visited = [False] * (n+1)
bfs(e, s, visited, path)

trace = s
while True:
    if visited[trace] == -1:
        break
    else:
        path.append(trace)
        trace = visited[trace]

print(len(path))