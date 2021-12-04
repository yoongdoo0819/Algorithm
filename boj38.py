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
    23 line에서 visited = [False] * (n+1), 
    31 line에서 if visited[dst] == False: 로 수정하면 결과는 틀림. 왜?
    visited[start] = 0으로 초기화하기 때문인듯. if 0 == False:는 True를 반환하기 때문에, start에 재방문될 수 있음
    그러나 visited = [-1] * (n+1)로 초기화하면 visited[start] = 0일 때, if 0 == -1: 코드는 False를 반환하므로 start 노드에 재방문하지 않음.
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