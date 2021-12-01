# 말이 되고픈 원숭이

"""
숨바꼭질 문제에서는 결과 값에 도달하기 까지 '벽'이 존재하지 않음
따라서 최대한 많은 곱셈을 통한 접근이 결과 값에 근접할 수 있음

본 문제에서는 가장 중요한 점이 n-1, m-1 좌표를 도달할 수 있는지 여부임.
n-1, m-1 좌표가 '벽'으로 둘러쌓인 경우, 인접 방문으로는 도달할 수 없으며 말의 움직임으로 벽을 건너 뛰어야만 함. 
즉, n-1, m-1 좌표에 도달하기 까지 얼마나 많은 벽들에 둘러 쌓일지 모르기 때문에,
처음부터 k번의 말의 움직임을 모두 소진하는 것은 최적의 결과가 아님.

따라서 숨바꼭질 (BOJ 1697) 문제와 다른 점은, 제한된 k를 적재적소에 사용해서 도착 지점에 도달하는 것.

즉, 본 문제 해결법은 
1.말의 움직임을 사용하지 않고 도달하는 경우  (0번째 map) 
2.말의 움직임을 한 번 사용해서 도달하는 경우 (1번째 map = 0번째 map에서 말의 움직임을 한 번 사용하여 1번째 map의 최단 거리 업데이트)
3.말의 움직임을 두 번 사용해서 도달하는 경우 (2번째 map = 1번째 map에서 ... )
4.말의 움직임을 k번 사용해서 도달하는 경우   (k번째 map = k-1번째 map에서 ...)
위와 같이 계산하기 위해 k개의 map을 사용. 즉, 3차원 배열 사용 
"""
from collections import deque

k = int(input())
m, n = map(int, input().split())

maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] == 1:
            maps[i][j] == -1

horse_xy = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [ [0 for _ in range(31) ] for _ in range(m) ] for _ in range(n) ]
visited[0][0][0] = 0

def bfs(x, y, k):
    q = deque()
    q.append((x, y, 0))
        
    while q:
        x, y, z = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][z]
            
        if z < k:    
            for i in range(8):
                horse_x, horse_y = horse_xy[i]
                horse_x += x 
                horse_y += y 
                
                if horse_x < 0 or horse_x >= n or horse_y < 0 or horse_y >= m:
                    continue
                
                if visited[horse_x][horse_y][z+1] == 0 and maps[horse_x][horse_y] == 0:
                    visited[horse_x][horse_y][z+1] = visited[x][y][z] + 1
                    q.append((horse_x, horse_y, z+1))    
                    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if visited[nx][ny][z] == 0 and maps[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
    
    return -1

print(bfs(0, 0, k))