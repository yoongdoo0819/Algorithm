# 치킨 배달 (BOJ 15686)

from itertools import combinations

n, m = map(int, input().split())
graph = []
chicken_houses = []
normal_houses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            chicken_houses.append((i, j))
        elif graph[i][j] == 1:
            normal_houses.append((i, j))  
    
answer = 1e9
for chicken_house_comb in combinations(chicken_houses, m):

    dist_table = [ [1e9] * n for _ in range(n) ]
    for chicken_house in chicken_house_comb:
        for normal_house in normal_houses:
            dist = abs(chicken_house[0] - normal_house[0]) + abs(chicken_house[1] - normal_house[1])
            if dist_table[normal_house[0]][normal_house[1]] > dist:
                dist_table[normal_house[0]][normal_house[1]] = dist
                
    temp_dist = 0
    for i in range(n):
        for j in range(n):
            if dist_table[i][j] != 1e9:
                temp_dist += dist_table[i][j]
    
    answer = min(answer, temp_dist)
    
print(answer)