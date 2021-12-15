# 계란으로 계란치기 (BOJ 16987)

n = int(input())
graph = []

for i in range(n):
    durability, weight = map(int, input().split())
    graph.append([durability, weight])
    
total_max_val = 0
def dfs(i, max_val):
    global total_max_val
    
    if i == n:
        total_max_val = max(total_max_val, max_val)
        return
    
    durability, weight = graph[i]
    if durability <= 0:
        dfs(i+1, max_val)
        return
    
    for next in range(0, n):
        if i == next:
            continue
        next_durability, next_weight = graph[next]
        if next_durability <= 0:
            dfs(i+1, max_val)
            
        elif durability > 0 and next_durability > 0:
            temp_next_durability = next_durability - weight
            temp_durability = durability - next_weight
            
            if temp_durability <= 0 and temp_next_durability <= 0:
                graph[i][0] = temp_durability
                graph[next][0] = temp_next_durability
                dfs(i+1, max_val+2)
                graph[i][0] = durability
                graph[next][0] = next_durability
            
            elif temp_durability <= 0 or temp_next_durability <= 0:
                graph[i][0] = temp_durability
                graph[next][0] = temp_next_durability
                dfs(i+1, max_val+1)
                graph[i][0] = durability
                graph[next][0] = next_durability
            
            elif temp_durability > 0 and temp_next_durability > 0:
                graph[i][0] = temp_durability
                graph[next][0] = temp_next_durability
                dfs(i+1, max_val)
                graph[i][0] = durability
                graph[next][0] = next_durability
               
        
dfs(0, 0)
print(total_max_val)