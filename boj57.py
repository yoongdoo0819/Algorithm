# 트리 순회 (BOJ 22856) (못품)

import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [ [] for _ in range(n+1) ]

for _ in range(n):
    root, left_child, right_child = map(int, input().split())
    graph[root].append(left_child)
    graph[root].append(right_child)
    
last_node = 1
    
def inorder(root):
    global a
    global last_node
    
    if root == -1:
        return
    
    child_list = graph[root]
    left_child = child_list[0]
    right_child = child_list[1]
    
    inorder(left_child)
    last_node = root
    inorder(right_child)

visited = [False] * (n+1)
cnt = 0
def dfs(start):
    global cnt
    
    visited[start] = True
    if start == last_node:
        print(cnt)
        exit()
        
    for next in graph[start]:
        if next != -1 and not visited[next]:
            cnt += 1
            dfs(next)
            cnt += 1
    

inorder(1)
print(last_node)
dfs(1)
