# 바이러스

n = int(input())
nets = int(input())
maps = [ [] for _ in range(n+1)]
visit = [False] * (n+1)

for net in range(nets):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)
    
def dfs(start, answer):
    visit[start] = True
    
    for nextNode in maps[start]:
        if visit[nextNode] != True:
            answer = dfs(nextNode, answer)
            answer += 1
    
    return answer
    
print( dfs(1, 0) )
