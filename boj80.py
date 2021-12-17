# 스도쿠 (BOJ 2580)

from collections import defaultdict

graph = [] # [] for _ in range(9) ]
zero_list = defaultdict(list)
idx = 0

for i in range(9):
    graph.append(list(map(int, input().split())))
    for j in range(9):
        if graph[i][j] == 0:
            zero_list[idx] = (i, j)
            idx += 1
            
def get_candidate(i, j):
    candidates = [1,2,3,4,5,6,7,8,9]
    
    for k in range(9):
        if graph[i][k] in candidates:
            candidates.remove(graph[i][k])
        if graph[k][j] in candidates:
            candidates.remove(graph[k][j])
            
    i //= 3
    j //= 3
    for k in range(i*3, (i+1)*3):
        for l in range(j*3, (j+1)*3):
            if graph[k][l] in candidates:
                candidates.remove(graph[k][l])
    return candidates

def dfs(idx):
    
    if idx == len(zero_list):
        for row in graph:
            print(*row)
        exit(0)
        
    i, j = zero_list[idx]
    candidate = get_candidate(i, j)
    
    for num in candidate:
        graph[i][j] = num
        dfs(idx+1)
        graph[i][j] = 0
    
dfs(0)