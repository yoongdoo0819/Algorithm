# 마법사 상어와 블리자드 (BOJ 21611) (못품)

n, m = map(int, input().split())

graph = [ [0] * n for _ in range(n) ]

graph[n//2][n//2] = -1

left, right = 2, 0
up, down = 0, 2
x = n//2-1
y = n//2-2
#graph[x][y] = 1
#while True:

while True:
    down = left
    x += 1
    y += 1
    if x < 0 or y < 0:
        break
    
    step = 0
    print("1 x, y", x, y)
    while step < down:
        graph[x][y] = graph[x][y] + 1
        x += 1
        step += 1

    for row in graph:
        print(row)
    right = down
    x -= 1
    y += 1
    step = 0
    print("2 x, y", x, y)
    while step < right:
        graph[x][y] = graph[x][y] + 1
        y += 1
        step += 1

    for row in graph:
        print(row)
    up = right
    x -= 1
    y -= 1
    step = 0
    print("3 x, y", x, y)
    while step < up:
        graph[x][y] = graph[x][y] + 1
        x -= 1
        step += 1

    for row in graph:
        print(row)
    left = up + 1
    x += 1
    y -= 1
    step = 0
    print("4 x, y", x, y)
    while step < left:
        graph[x][y] = graph[x][y] + 1
        y -= 1
        step += 1
    
    for row in graph:
        print(row)

    