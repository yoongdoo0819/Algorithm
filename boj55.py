# 빗물 (BOJ 14719)

n, m = map(int, input().split())
blocks = list(map(int, input().split()))

graph = [ [0] * m for _ in range(n) ]


idx = 0
for block in blocks:
    
    h = n-1
    for _ in range(block):
        graph[h][idx] = 1
        h -= 1
    idx += 1

total_rain = 0
# 맵 위에서부터 행 하나씩 탐색 (만약 벽돌이 아래에 안 쌓여있다면 위에도 쌓일리가 없으므로, 현실 상황이랑 맞지 않음)
for i in range(n):
    k = 1
    for j in range(0, m, k):
        # 현재 탐색 위치에 벽돌이 존재한다면 
        if graph[i][j] == 1:
            k = j + 1
            rain = 0
            # 오른쪽 끝까지 탐색하면서 벽돌이 동일한 높이에 존재하는지 확인
            while k < m:
                if graph[i][k] == 0:
                    graph[i][k] = 2
                    rain += 1
                    k += 1
                # 오른쪽에도 벽돌이 존재한다면 빗물이 고일 수 있다는 뜻
                elif graph[i][k] == 1:
                    total_rain += rain
                    break


print(total_rain)