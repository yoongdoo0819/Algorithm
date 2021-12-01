# ABCDE

n, m = map(int, input().split())

maps = [ [] for _ in range(n)]

for _ in range(m):
    src, dst = map(int, input().split())
    maps[src].append(dst)
    maps[dst].append(src)
    
def dfs(start, depth, visited):
    visited[start] = True
    
    if depth == 5:
        print(1)
        exit()
    
    for next in maps[start]:
        if not visited[next]:
            dfs(next, depth+1, visited)
            visited[next] = False

for i in range(n):
    visited = [False] * (n)
    dfs(i, 1, visited)
    
print(0)