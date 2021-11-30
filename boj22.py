# 숨바꼭질 (BOJ 1697)

from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    
    while q:
        pos = q.popleft()
        if pos == k:
            print(visited[pos])
            
        for next_pos in [pos+1, pos-1, pos*2]:
            if 0 <= next_pos <= MAX:
                if visited[next_pos] == -1:
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)
                
bfs(n)