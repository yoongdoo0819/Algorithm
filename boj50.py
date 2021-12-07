# 배열 돌리기 1 (BOJ 16926)

n, m, r = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))
    
    
def rotate():
    visited = [ [-1] * m for _ in range(n) ]
    backup_x, backup_y = -1, -1
    cnt = 0
    
    while cnt < (min(n, m) / 2):
        
        """
        15 line의 while문 탈출 조건을 아래와 같이 적용하면 시간 초과 발생
        cnt = 0
        for visit in visited:
            cnt += visit.count(1)
            
        if cnt == n*m:
            break
        """
        
        backup_x += 1
        backup_y += 1
        x, y = backup_x, backup_y
        if y+1 >= m or visited[x][y+1] == 1:
            break
        backup_val = maps[x][y+1]
        visited[x][y] = 1
        temp1 = maps[x][y]
        temp2 = -1
        
        while x+1 < n and visited[x+1][y] == -1:
            temp2 = maps[x+1][y]
            maps[x+1][y] = temp1
            visited[x+1][y] = 1
            x += 1
            temp1 = temp2
            
        while y+1 < m and visited[x][y+1] == -1:
            temp2 = maps[x][y+1]
            maps[x][y+1] = temp1
            visited[x][y+1] = 1
            y += 1
            temp1 = temp2
            
        while 0 <= x-1 and visited[x-1][y] == -1:
            temp2 = maps[x-1][y]
            maps[x-1][y] = temp1
            visited[x-1][y] = 1
            x -= 1
            temp1 = temp2

        while 0 <= y-1 and visited[x][y-1] == -1:
            temp2 = maps[x][y-1]
            maps[x][y-1] = temp1
            visited[x][y-1] = 1
            y -= 1
            temp1 = temp2
            
        maps[backup_x][backup_y] = backup_val
    
for _ in range(r):
    rotate()
    
for map in maps:
    for val in map:
        print(val, end = ' ')
    print("")