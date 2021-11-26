# DFS와 BFS

from collections import deque
 
n, m, start = map(int, input().split())
maps = [ [] for _ in range(n+1) ]

for _ in range(m):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)
    
for map in maps:
    map.sort()
    
dfs_list = []
def dfs(start, visited):
    visited[start] = True
    dfs_list.append(start)
    
    for next in maps[start]:
        if not visited[next]:
            dfs(next, visited)
            
bfs_list = []
def bfs(start, visited):
    
    visited[start] = True
    queue = deque()
    queue.append(start)
    bfs_list.append(start)
    
    while queue:
        node = queue.popleft()
        
        for next in maps[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                bfs_list.append(next)

visited = [False] * (n+1)
dfs(start, visited)
for node in dfs_list:
    print(node, end = ' ')

print("")
visited = [False] * (n+1)
bfs(start, visited)
for node in bfs_list:
    print(node, end = ' ')
    