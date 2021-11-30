# 숨바꼭질3 

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
            return
            
        for next_pos in [pos*2, pos+1, pos-1]:
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:
                if pos*2 == next_pos :
                    visited[next_pos] = visited[pos]
                    """
                    *2에 해당하는 값을 방문할 때는 +1을 안 해주므로,
                    +나 -보다 최우선으로 방문해야 k가 되었을 때 최솟값이 됨.
                    따라서 append가 아닌 appendleft를 통해 *2인 경우에는 
                    +나 -보다 가장 먼저 queue에서 뽑힐 수 있도록 하는 것이 중요
                    """
                    q.appendleft(next_pos) 
                    
                elif pos+1 == next_pos :
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)
                
                elif pos-1 == next_pos :
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)
                    
bfs(n)