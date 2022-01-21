# A → B (BOJ 16953)

from collections import deque

start, target = map(int, input().split())

def bfs(start, target):
    q = deque()
    q.append((start, 1))
    
    while q:
        val, cnt = q.popleft()
        if val == target:
            return cnt
        elif val > target:
            continue
        
        q.append((int(str(val)+'1'), cnt+1))
        q.append((val*2, cnt+1))
        
    return -1

print(bfs(start, target))