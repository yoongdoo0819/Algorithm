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
for i in range(n):
    k = 1
    for j in range(0, m, k):
        if graph[i][j] == 1:
            k = j + 1
            rain = 0
            while k < m:
                if graph[i][k] == 0:
                    graph[i][k] = 2
                    rain += 1
                    k += 1
                elif graph[i][k] == 1:
                    total_rain += rain
                    break


print(total_rain)