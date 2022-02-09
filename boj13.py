# 숨바꼭질3 (BOJ 13549)

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

"""
아래 BFS는 정답이 안 됨.
if x-1 < 0 or x+1 < 0 or x*2 < 0 or x-1 > 100000 or x+1 > 100000 or x*2 > 100000: continue와 같은 코드는
만약 x가 60000이라면 x+1 > 100000 조건을 만족하지 못함. 그러나, x*2 > 100000 조건을 만족하기 때문에 continue를 실행하게 됨.
즉 *, +, - 연산을 다음과 같이 개별적으로 수행해야만 정답이 됨.
        # if 0 <= x*2 <= 100000 and not visited[x*2]:    
        #     visited[x*2] = True
        #     q.appendleft((x*2, time))
                
        # if 0 <= x+1 <= 100000 and not visited[x+1]:
        #     visited[x+1] = True
        #     q.append((x+1, time+1))
        
        # if 0 <= x-1 <= 100000 and not visited[x-1]:
        #     visited[x-1] = True
        #     q.append((x-1, time+1))
         
            
from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
def bfs(start, time):
    
    q = deque()
    q.append((start, time))
    visited[start] = True
    
    while q:
        x, time = q.popleft()
        
        if x == K:
            return time
        
        if x-1 < 0 or x+1 < 0 or x*2 < 0 or x-1 > 100000 or x+1 > 100000 or x*2 > 100000:
            continue
        
        if not visited[x*2]:
            visited[x*2] = True
            q.appendleft((x*2, time))
            
        if not visited[x+1]:
            visited[x+1] = True
            q.append((x+1, time+1))
        
        if not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, time+1))
            
            
time = bfs(N, 0)
print(time)

"""