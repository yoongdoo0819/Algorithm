# 숨바꼭질2 (BOJ 12851)

from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX+1)
cnt = 0
result = 0

def bfs(start):
    global cnt
    global result
    
    q = deque()
    q.append(start)
    visited[start] = 0
    
    while q:
        pos = q.popleft()
        
        if pos == k:
            result = visited[pos]
            cnt += 1  
        
        for next_pos in [pos+1, pos-1, pos*2]:
            if 0 <= next_pos <= MAX:
                
                if visited[next_pos] == -1 or visited[next_pos] == visited[pos] + 1 :# or next_pos == k:
                    
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)
                
bfs(n)
print(result)
print(cnt)