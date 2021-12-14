# 외판원 순회 2 (BOJ 10971)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
min_val = 1e9
def dfs(start, src, visited):
    global min_val
    global one_path_min_val
    
    if len(visited) == n:
        if graph[src][start] > 0:
            one_path_min_val += graph[src][start]
            min_val = min(min_val, one_path_min_val)
            one_path_min_val -= graph[src][start]
        return
        
    for dst in range(0, n): 
        if not dst in visited and graph[src][dst] > 0:
            visited.add(dst) 
            one_path_min_val += graph[src][dst]
            dfs(start, dst, visited)
            one_path_min_val -= graph[src][dst]
            visited.remove(dst)
    
visited = set()
for i in range(n):
    
    visited.add(i)
    one_path_min_val = 0
    dfs(i, i, visited)
    visited.remove(i)
    
print(min_val)
