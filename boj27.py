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
            """
            0-1
            1-2
            2-3
            0-3
            1-4
            위와 같은 그래프에서 (1). 0->1->2->3 순서로 탐색하면 depth가 4이므로 실패.
            (2). 0->3->2->1->4 순서로 탐색하면 성공.
            그러나 (1)번에서 1, 2, 3 노드를 방문했던 정보 True를 그대로 유지하고 있다면 (2)과 같이 재탐색할 수 없음
            따라서 방문하려는 노드 (next)를 기준으로 dfs를 다시 호출하는 경우, 
            해당 dfs가 종료된 이후에는 방문 정보를 False로 다시 변경해줘야 함 
            
            즉, 첫 방문 노드에서 연결된 모든 노드를 재귀적으로 방문 시, 방문 순서에 따라 가장 깊은 depth가 달라질 수 있으므로,
            방문했던 노드 정보를 다시 False로 변경해주고 가장 깊은 depth가 5가 될 수 있는 경로가 존재하는지 확인해야 함 
            """
            visited[next] = False

for i in range(n):
    visited = [False] * (n)
    dfs(i, 1, visited)
    
print(0)