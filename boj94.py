# 링크와 스타트 (BOJ 15661)

from itertools import combinations

n = int(input())
graph = []
min_diff = 1e9

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(1, n//2+1):
    
    for start_member in combinations([idx for idx in range(n)], i):
    
        link_member = list(set([idx for idx in range(n)]) - set(start_member))
        
        start_ability, link_ability = 0, 0
        for i, j in combinations(list(start_member), 2):
            start_ability += graph[i][j] + graph[j][i]
        
        for i, j in combinations(list(link_member), 2):
            link_ability += graph[i][j] + graph[j][i]
            
        min_diff = min(min_diff, abs(start_ability - link_ability))
            
            
            
print(min_diff)
