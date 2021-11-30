# 숨바꼭질4 

from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX+1)
prev_node = [-1] * (MAX+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    prev_node[start] = False
    
    while q:
        pos = q.popleft()
        if pos == k:
            print(visited[pos])
            break
            
        for next_pos in [pos+1, pos-1, pos*2]:
            if 0 <= next_pos <= MAX:
                if visited[next_pos] == -1:
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)
                    
                    if prev_node[next_pos] == -1:
                        prev_node[next_pos] = pos
                
bfs(n)
reverse = deque()
if k != -1:
    reverse.append(k)
    while True:
        parent = prev_node[k]
        if parent == False:
            break
        else:
            #print(parent, end=' ')
            reverse.appendleft(parent)
            k = parent
            
for v in reverse:
    print(v, end=' ')