# 테트로미노 (BOJ 14500)

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
block_dfs1_dx = [ (-1, 1, 0), (-1, 1, 0), (0, 0, -1), (0, 0, 1) ]
block_dfs1_dy = [ (0, 0, 1), (0, 0, -1), (-1, 1, 0), (-1, 1, 0) ]

block_dfs2_dx = [-1, 1, 0, 0]
block_dfs2_dy = [0, 0, -1, 1]

max_score = 0
visited = [ [False] * m for _ in range(n) ]

"""
ㅁ      ㅁ    ㅁ
ㅁㅁ  ㅁㅁ  ㅁㅁㅁ  ㅁㅁㅁ
ㅁ      ㅁ           ㅁ

위의 4개의 도형에 대한 dfs
"""
def block_dfs1(x, y, score):
    global max_score
    
    for i in range(4):
        
        check = True
        total_score = score
        for j in range(3):
            nx = x + block_dfs1_dx[i][j]
            ny = y + block_dfs1_dy[i][j]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                check = False
                break
            total_score += graph[nx][ny]
        
        if check == True:
            max_score = max(max_score, total_score)


def block_dfs2(x, y, depth, total_score):
    global max_score
    
    if depth == 3:
        max_score = max(max_score, total_score)
        return
    
    for i in range(4):
        nx = x + block_dfs2_dx[i]
        ny = y + block_dfs2_dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            block_dfs2(nx, ny, depth+1, total_score+graph[nx][ny])
            visited[nx][ny] = False    
        

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        block_dfs1(i, j, graph[i][j])
        block_dfs2(i, j, 0, graph[i][j])
        visited[i][j] = False
        
print(max_score)