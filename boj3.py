# 트리의 부모 찾기

n = int(input())
maps = [ [] for _ in range(n+1) ]
visited = {}

for _ in range(n-1):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)
    

#print(n)
#for idx in range(1, len(maps)):
#    print(idx, maps[idx])

def dfs(start):
    
    for child in maps[start]:
        visited[child] = start
        maps[child].remove(start)
        
    for child in maps[start]:
        dfs(child)
    
dfs(1)
for idx in range(2, n+1):
    print(visited[idx])
    
    