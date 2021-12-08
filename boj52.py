# 상어 초등학교 (BOJ 21608) 

from copy import deepcopy

n = int(input())

graph = [ [0] * n for _ in range(n) ]
friends_list = []

for _ in range(n*n):
    num, a, b, c, d = map(int, input().split())
    friends_list.append((num, a, b, c, d))
    
def max_xy():
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                return x, y
                
def arrange_seat(std, a, b, c, d):
    friend_seat_graph =  [ [0] * n for _ in range(n) ]
    empty_seat_graph =  [ [0] * n for _ in range(n) ]
    friend_check = False
    empty_check = False
    
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] in [a, b, c, d]:
                        friend_seat_graph[x][y] += 1
                        friend_check = True
                    if graph[nx][ny] == 0:
                        empty_seat_graph[x][y] += 1
                        empty_check = True
                        
    max_x, max_y = 0, 0
    # 인접한 곳이 자리가 꽉 차있으면서, 좋아하는 친구가 자리를 앉은 것도 아니라면
    if friend_check == False and empty_check == False:
        max_x, max_y = max_xy()
                    
    # 인접한 곳 중 좋아하는 친구가 있다면, 
    elif friend_check == True:
        max = -1e9
        max_val_cnt = 0
        
        # 좋아하는 친구가 가장 많이 인접한 자리에 착석
        for x in range(n):
            for y in range(n):
                if max < friend_seat_graph[x][y]:
                    max = friend_seat_graph[x][y]
                    max_x, max_y = x, y
        
        # 좋아하는 친구가 가장 많이 인접한 자리가 한 개인지 확인하고,
        for x in range(n):
            for y in range(n):
                if max == friend_seat_graph[x][y]:
                    max_val_cnt += 1
        
        # 좋아하는 친구가 가장 많이 인접한 자리가 두 개 이상이라면, 
        # 좋아하는 친구가 가장 많이 인접한 자리 중 주변에 비어있는 자리가 최대한 많은 곳에 착석 
        if max_val_cnt > 1:
            empty_max_val = -1e9
            for x in range(n):
                for y in range(n):
                    if friend_seat_graph[x][y] == max and empty_max_val < empty_seat_graph[x][y]:
                        empty_max_val = empty_seat_graph[x][y]
                        max_x, max_y = x, y         
    
    # 인접한 곳 중 좋아하는 친구는 없고 자리가 비어있다면, 주변에 비어있는 자리가 최대한 많은 곳에 착석     
    elif friend_check == False:
        empty_max_val = -1e9
        for x in range(n):
            for y in range(n):
                if empty_max_val < empty_seat_graph[x][y]:
                    empty_max_val = empty_seat_graph[x][y]
                    max_x, max_y = x, y
                    
    graph[max_x][max_y] = std
    
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for friend in friends_list:
    std, a, b, c, d = friend
    arrange_seat(std, a, b, c, d)
    
    
score_graph = [ [-1] * n for _ in range(n) ]
total_score = 0
for x in range(n):
    for y in range(n):
        for friend in friends_list:
            std, a, b, c, d = friend
            if graph[x][y] == std:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] in [a, b, c, d]:
                        cnt += 1
                if cnt == 0:
                    score_graph[x][y] = 0
                elif cnt == 1:
                    score_graph[x][y] = 1
                elif cnt == 2:
                    score_graph[x][y] = 10
                elif cnt == 3:
                    score_graph[x][y] = 100
                elif cnt == 4:
                    score_graph[x][y] = 1000
                total_score += score_graph[x][y]

print(total_score)
