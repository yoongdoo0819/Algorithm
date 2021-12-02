# 움직이는 미로 탈출

from collections import deque

n, m = 8, 8
maps = []

for _ in range(n):
    maps.append(input())
    
dx = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 0, -1, 1, 1, -1, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        
        visited = [ [False] * m for _ in range(n) ] 
        
        for _ in range(len(q)):
            x, y = q.popleft()
            """
            #visited[x][y] = True
            
            큐에서 x,y 좌표 pop 이후 즉시 방문 정보를 True로 설정하면 안 됨.
            맵의 형태가 매번 변경되므로 x,y와 인접한 노드에서 x,y를 방문할 수 있도록
            해줘야 함. pop 이후 방문 정보를 즉시 True로 설정하면, x,y와 인접한 노드에서
            x,y를 방문할 수 없음.
            그러나 x,y와 인접한 노드(e.g., a)에서 x,y를 방문할 기회가 있다면 아래 for문을 실행하면서
            방문을 할 것이고, 그때 x,y 방문 정보를 True로 설정하게 됨. 이후에는
            x,y와 인접한 또 다른 노드(e.g., b)에서 x,y를 방문할 기회가 존재한다고 할지라도
            이미 이전에 a 노드에서 x,y를 방문했고 큐에 삽입하였으므로,
            b 노드에서는 x,y를 또 닷 큐에 삽입하는 것은 중복처리가 됨.
            
            """
            if maps[x][y] == '#':
                continue
                
            if x == 0 and y == 7:
                return 1
            
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[nx][ny] == '#':
                    continue
                
                if maps[nx][ny] == '.' and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    
        maps.pop()
        maps.insert(0, '........')
        
    return 0

print(bfs(7, 0))
