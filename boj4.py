# 효율적인 해킹

"""
아래 DFS로는 못 푸는지 ?
시간/메모리 제한에서 걸림

import sys 
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graphs = [ [] for _ in range(N+1) ]

for _ in range(M):
    src, dst = map(int, input().split())
    graphs[dst].append(src)
    
ans = [ 0 for _ in range(N+1) ]
def dfs(src, cnt):
    
    for dst in graphs[src]:
        if not visited[dst]:
            visited[dst] = True
            cnt = dfs(dst, cnt+1)
            
    return cnt

for i in range(1, N+1):
    visited = [False] * (N+1)
    ans[i] = dfs(i, 0)
    
max_val = max(ans)
for i in range(1, N+1):
    if max_val == ans[i]:
        print(i, end=' ')
            

"""
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
    
