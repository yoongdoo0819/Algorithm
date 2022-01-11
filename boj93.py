# 스타트와 링크 (BOJ 14889)

from itertools import combinations

n = int(input())
graph = []
min_diff = 1e9
members = list(combinations([i for i in range(n)], n//2))

for _ in range(n):
    graph.append(list(map(int, input().split())))
    

for member in members:
    start_member = list(member)
    link_member = list(set([i for i in range(n)]) - set(start_member))
    
    start_ability = 0
    for i, j in combinations(start_member, 2):
        start_ability += graph[i][j] + graph[j][i] 
    
    link_ability = 0
    for i, j in combinations(link_member, 2):
        link_ability += graph[i][j] + graph[j][i]
    
    min_diff = min(min_diff, abs(start_ability - link_ability))
    

print(min_diff)