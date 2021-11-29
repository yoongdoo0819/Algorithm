# 특정 거리의 도시 찾기

import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

maps = [ [] for _ in range(n+1) ]
""" 
맨 처음 start 노드에서 시작,
이때, visited를 모두 0으로 초기화했다면,  
43 line에서 if visited[next] == 0 코드에 의해
start 노드와 연결된 노드가 start 노드를 다시 방문함.
다시 방문하게 되면 start 노드의 거리 (visited[start]) 값이 변경되고, 
결국 최종 결과에 영향을 미치게 됨. 
따라서 start를 다시 방문하는 경우에는, 40 line에서와 같이  
재차 방문하지 못하도록 해야함. 
40 line을 제외하려면, visited를 초기화(23~24 line)할 때 start 노드를 제외한 
모든 노드는 -1로 초기화하여 start 노드와 아직 방문하지 않은 
노드들에 대한 거리 정보를 차별화하면 됨. 또한, 43 lien은 if visited[next] == -1로 수정
""" 
visited = [0] * (n+1)
visited[x] = 0

for _ in range(m):
    src, dst = map(int, input().split())
    maps[src].append(dst)

shortest_path = []
def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        
        for next in maps[v]:
            
            if next == start: 
                continue
                
            if visited[next] == 0:
                visited[next] = visited[v] + 1
                q.append(next)
                if visited[next] == k:
                    shortest_path.append(next)

bfs(x)

if shortest_path:
    shortest_path.sort()
    for path in shortest_path:
        print(path)
else:
    print(-1)
