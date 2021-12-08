# 상어 초등학교 (BOJ 21608) (못품)

n = int(input())

graph = [ [0] * n for _ in range(n) ]
friends_list = []

for _ in range(n*n):
    num, a, b, c, d = map(int, input().split())
    friends_list.append((num, a, b, c, d))
    
def arrange_seat(std, a, b, c, d):
    friend_seat_graph = [ [0] * n for _ in range(n) ]
    empty_seat_graph = [ [0] * n for _ in range(n) ]
    check = False
    
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
                        check = True
                    if graph[nx][ny] == 0:
                        empty_seat_graph[x][y] += 1
                        
    max_x, max_y = -1, -1
    if check == True:
        max = -1e9
        max_val_cnt = 0
        for x in range(n):
            for y in range(n):
                if max < friend_seat_graph[x][y]:
                    max = friend_seat_graph[x][y]
        
        for x in range(n):
            for y in range(n):
                if max == friend_seat_graph[x][y]:
                    max_val_cnt += 1
        
        if max_val_cnt > 1:
            empty_max_val = -1e9
            for x in range(n):
                for y in range(n):
                    if friend_seat_graph[x][y] == max and empty_max_val < empty_seat_graph[x][y]:
                        empty_max_val = empty_seat_graph[x][y]
                        max_x, max_y = x, y
        elif max_val_cnt == 1:
            for x in range(n):
                for y in range(n):
                    if friend_seat_graph[x][y] == max:
                        max_x, max_y = x, y
                        
                        
    elif check == False:
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
