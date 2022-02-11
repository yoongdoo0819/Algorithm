# 바이러스 (BOJ 2606)

"""
DFS와 BFS 풀이 모두에서
maps[x].append(y)로 방향 그래프를 연결하지만,
maps[y].append(x)도 추가하여 무방향 그래프를 연결해야만 정답이 되는 이유?
단방향 그래프에서는 왜 정답이 못 되는지 ?

입력 값이 아래와 같은 경우,
4
3
1 2
2 3
4 2
무방향이면 답은 3, 단방향이면 답은 2가 나옴.

"""

"""
아래는 DFS 풀이

"""
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

"""
아래는 BFS로 풀이

from collections import deque

N = int(input())
number_of_pairs = int(input())

graphs = [ [] for _ in range(101) ]

for _ in range(number_of_pairs):
    src, dst = map(int, input().split())
    graphs[src].append(dst)
    graphs[dst].append(src)
visited = [False] * 101

def bfs(start, cnt):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        src = q.popleft()
        
        for dst in graphs[src]:
            if not visited[dst]:
                visited[dst] = True
                q.append(dst)
                cnt += 1

    return cnt


print(bfs(1, 0))

"""