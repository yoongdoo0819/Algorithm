# 배열 돌리기 (BOJ 17276)

from collections import deque

t = int(input())

def left_rotate(count):
    for _ in range(count):
        q = deque()
        for i in range(n):
            q.append(graph[i][i])
            
        mid = n//2
        for i in range(n):
            graph[i][i] = graph[i][mid]
            
        for i in range(n):
            graph[i][mid] = graph[i][n-1-i]
            
        for i in range(n):
            graph[n-1-i][i] = graph[mid][i]
            
        for i in range(n):
            val = q.popleft()
            graph[mid][i] = val
                
                
def right_rotate(count):
    for _ in range(count):
        q = deque()
        for i in range(n):
            q.append(graph[i][i])
            
        mid = n//2
        for i in range(n):
            graph[i][i] = graph[mid][i]
            
        for i in range(n):
            graph[mid][i] = graph[n-1-i][i]
            
        for i in range(n):
            graph[i][n-1-i] = graph[i][mid]
            
        for i in range(n):
            val = q.popleft()
            graph[i][mid] = val
                
                
for _ in range(t):
    n, d = map(int, input().split())
    graph = []
    
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    if d < 0:
        left_rotate(abs(d)//45)
    else:
        right_rotate(d//45)
    
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end = ' ')
        print("")
        
    