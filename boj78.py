# N-Queen (BOJ 9663)

n = int(input())

graph = [0] * n
visited = [False] * n

cnt = 0

def check(k):
    for i in range(k):
        if (graph[k] == graph[i]) or (abs(graph[k] - graph[i]) == k - i):
            return False
    return True

def dfs(idx):
    global cnt
    
    if idx == n:
        cnt += 1
        return
    
    for i in range(n):
        
        if visited[i]:
            continue
        
        graph[idx] = i
        if check(idx):
            visited[i] = True
            dfs(idx+1)
            visited[i] = False
            
dfs(0)
print(cnt)