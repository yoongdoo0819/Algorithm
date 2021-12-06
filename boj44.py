# 달팽이 (BOJ 1913)

n = int(input())
maps = [ [0] * n for _ in range(n) ]
target = int(input())

val = n ** 2
loc = 'down'
x, y = 0, 0

while val > 0:
    if loc == 'down':
        while (0 <= x and x < n and 0 <= y and y < n) and maps[x][y] == 0:
            maps[x][y] = val
            val -= 1
            x += 1
        x -= 1
        loc = 'right'
        y += 1
    elif loc == 'right':
        while (0 <= x and x < n and 0 <= y and y < n) and maps[x][y] == 0:
            maps[x][y] = val
            val -= 1
            y += 1
        y -= 1
        loc = 'up'
        x -= 1
    elif loc == 'up':
        while (0 <= x and x < n and 0 <= y and y < n) and maps[x][y] == 0:
            maps[x][y] = val
            val -= 1
            x -= 1
        x += 1
        loc = 'left'
        y -= 1
    elif loc == 'left':
        while (0 <= x and x < n and 0 <= y and y < n) and maps[x][y] == 0:
            maps[x][y] = val
            val -= 1
            y -= 1
        y += 1
        loc = 'down'
        x += 1
    
        
x, y = 0, 0
for i in range(n):
    for j in range(n):
        print(maps[i][j], end = ' ')
        if target == maps[i][j]:
            x = i+1
            y = j+1
    print("")
    
print(x, y)
    