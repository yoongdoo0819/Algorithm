# 무기 공학 (BOJ 18430)

from copy import deepcopy

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
max_val = 0

def dfs(cnt, graph, sum_val):
    global max_val
    
        
    if cnt == n*m:
        max_val = max(max_val, sum_val)
        return
    
    x, y = cnt//m, cnt%m
    
    dfs(cnt+1, deepcopy(graph), sum_val)
    
    """
    deepcopy(graph)는 성공
    그러나 graph.copy()는 실패
    """
    if graph[x][y] > 0:
        if x-1 >= 0 and y-1 >= 0 and graph[x-1][y] > 0 and graph[x][y-1] > 0:
            temp_graph = deepcopy(graph) #.copy()
            temp_sum_val = graph[x-1][y] + graph[x][y]*2 + graph[x][y-1]
            sum_val += temp_sum_val
            temp_graph[x-1][y] = 0
            temp_graph[x][y-1] = 0
            temp_graph[x][y] = 0
            dfs(cnt+1, temp_graph, sum_val)
            sum_val -= temp_sum_val
        
        if x-1 >= 0 and y+1 < m and graph[x-1][y] > 0 and graph[x][y+1] > 0:
            temp_graph = deepcopy(graph) #.copy()
            temp_sum_val = graph[x-1][y] + graph[x][y]*2 + graph[x][y+1]
            sum_val += temp_sum_val
            temp_graph[x-1][y] = 0
            temp_graph[x][y+1] = 0
            temp_graph[x][y] = 0
            dfs(cnt+1, temp_graph, sum_val)
            sum_val -= temp_sum_val
        
        if x+1 < n and y-1 >= 0 and graph[x+1][y] > 0 and graph[x][y-1] > 0:
            temp_graph = deepcopy(graph) #.copy()
            temp_sum_val = graph[x+1][y] + graph[x][y]*2 + graph[x][y-1]
            sum_val += temp_sum_val
            temp_graph[x+1][y] = 0
            temp_graph[x][y-1] = 0
            temp_graph[x][y] = 0
            dfs(cnt+1, temp_graph, sum_val)
            sum_val -= temp_sum_val
            
        if x+1 < n and y+1 < m and graph[x+1][y] > 0 and graph[x][y+1] > 0:
            temp_graph = deepcopy(graph) #.copy()
            temp_sum_val = graph[x+1][y] + graph[x][y]*2 + graph[x][y+1]
            sum_val += temp_sum_val
            temp_graph[x+1][y] = 0
            temp_graph[x][y+1] = 0
            temp_graph[x][y] = 0
            dfs(cnt+1, temp_graph, sum_val)
            sum_val -= temp_sum_val
  
    
dfs(0, graph, 0)
print(max_val)