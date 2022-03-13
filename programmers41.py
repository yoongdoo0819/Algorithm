# 전력망을 둘로 나누기

from collections import deque

def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 1
    
    while q:
        x = q.popleft()
    
        for next_node in graph[x]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                cnt += 1
    return cnt

def add_graph(graph, wire):
    x, y = wire
    graph[x].append(y)
    graph[y].append(x)
    
    return graph

def cut_graph(graph, wire):
    x, y = wire
    graph[x].remove(y)
    graph[y].remove(x)
    
    return graph

def solution(n, wires):
    ans = 1e9
    
    graph = [ [] for _ in range(n+1) ]
    for wire in wires:
        x, y = wire
        graph[x].append(y)
        graph[y].append(x)
        
    for wire in wires:
        temp_graph = cut_graph(graph, wire)
        
        cnt = 0
        visited = [False] * (n+1)
        cnt = bfs(1, temp_graph, visited)
        
        min_val = abs(n - cnt)
        min_val = abs(min_val - cnt)
        ans = min(ans, min_val)
        
        graph = add_graph(temp_graph, wire)
    
    return ans