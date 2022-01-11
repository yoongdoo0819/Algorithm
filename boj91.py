# 꽃길 (BOJ 14620)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [False] * n for _ in range(n) ]
answer = 1e9

def is_visited(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return False
        if visited[nx][ny] == True:
            return False
    
    return True

def visited_check(x, y):

    if visited[x][y] == False:
        visited[x][y] = True
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if visited[nx][ny] == False:
            visited[nx][ny] = True
        

def visited_uncheck(x, y):
    
    if visited[x][y] == True:
        visited[x][y] = False
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if visited[nx][ny] == True:
            visited[nx][ny] = False
        
    
def calc_cost(x, y):
    cost = graph[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        cost += graph[nx][ny]
            
    return cost
    
def dfs(start, cost, cnt):
    global answer
    
    if cnt == 3:
        answer = min(answer, cost)    
        return

    for x in range(start, n):
        for y in range(n):
            
            if visited[x][y] == False and is_visited(x, y) == True:
                visited_check(x, y)
                dfs(x, cost + calc_cost(x, y), cnt+1)
                visited_uncheck(x, y)
                
dfs(0, 0, 0)
print(answer)