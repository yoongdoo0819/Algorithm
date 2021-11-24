# 거리두기 확인하기

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(place, row, col):
    q = deque()
    q.append((row, col, 0))
    visit_map = [ [0] * 5 for _ in range(5) ]
    visit_map[row][col] = True
    
    while q:
        row, col, cnt = q.popleft()
            
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if place[nx][ny] == 'X':
                continue
            if not visit_map[nx][ny] and place[nx][ny] == 'P':
                return False
            
            for j in range(4):
                nnx = nx + dx[j]
                nny = ny + dy[j]

                if nnx < 0 or nnx > 4 or nny < 0 or nny > 4:
                    continue
                if place[nnx][nny] == 'X':
                    continue
                if not visit_map[nnx][nny] and place[nnx][nny] == 'P':
                    return False
            
    return True

def all_visit_map(place):
    
    for row in range(len(place)):
        for col in range(len(place[0])):
            if place[row][col] == 'P':
                if bfs(place, row, col) == False:
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if all_visit_map(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer