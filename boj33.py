# 직사각형 탈출 (BOJ 16973)

"못품. 문제가 뭔지?"

from collections import deque

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

h, w, s1, s2, d1, d2 = map(int, input().split())
s1 -= 1
s2 -= 1
d1 -= 1
d2 -= 1


xy_list = []
q = deque()
for i in range(s1, h):
    for j in range(s2, w):
        xy_list.append(i)
        xy_list.append(j)

q.append(xy_list)
num = h*w
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    step = 0
    visited_list = []
    visited_list.append(xy_list)
        
    while q:
        
        for _ in range(len(q)):
            xy = q.popleft()
            
            for move_idx in range(4):
                cnt = 0    
                move_list = []
                
                for xy_idx in range(0, len(xy), 2):
                    x = xy[xy_idx]
                    y = xy[xy_idx+1]
                    nx = x + dx[move_idx]
                    ny = y + dy[move_idx]
            
                    if x == d1 and y == d2 and xy_idx == 0 and xy_idx+1 == 1:
                        return step
                        
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    
                    if maps[nx][ny] == 1:
                        continue
                    
                    if maps[nx][ny] == 0 : #and nx in xy and ny in xy:
                        cnt += 1
                        move_list.append(nx)
                        move_list.append(ny)
                   
                if cnt == num :
                    if not move_list in visited_list :
                        q.append(move_list)
                        visited_list.append(move_list)
                        
        step += 1
        
    return -1
            
print(bfs())
