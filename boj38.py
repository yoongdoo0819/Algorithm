# 트리의 지름 (BOJ 1967)

from collections import deque

n = int(input())
maps = [ [] for _ in range(n+1) ] 

for _ in range(n-1):
    src, dst, weight = map(int, input().split())
    maps[src].append((dst, weight))
    maps[dst].append((src, weight))
 
 
def bfs(start):
    q = deque()
    q.append(start)
    """
    21 line에서 visited = [False] * (n+1), 
    29 line에서 if visited[dst] == False: 로 수정하면 결과는 틀림. 왜?
    """
    visited = [-1] * (n+1) 
    visited[start] = 0
    max_val = [0, 0]
    
    while q:
        src = q.popleft()
        
        for dst, weight in maps[src]:
            if visited[dst] == -1:
                visited[dst] = visited[src] + weight
                q.append(dst)
                if max_val[0] < visited[dst]:
                    max_val = visited[dst], dst
    return max_val

max_dist, node = bfs(1)
max_dist, node = bfs(node)
print(max_dist)