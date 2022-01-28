# 링크와 스타트 (BOJ 15661)

"""
아래는 dfs를 활용하여 해결
"""

N = int(input())
teams = []
ans = 1e9

for _ in range(N):
    teams.append(list(map(int, input().split())))

def dfs(start_team, idx, cnt):
    global ans
    
    if start_team:
        link_team = [i for i in range(N)]
        for i in start_team:
            link_team.remove(i)
        
        start_team_ability = 0
        for i in start_team:
            for j in start_team:
                start_team_ability += teams[i][j]
                
        
        link_team_ability = 0
        for i in link_team:
            for j in link_team:
                link_team_ability += teams[i][j]
                
        ans = min(ans, abs(start_team_ability-link_team_ability))
        
        
    for i in range(idx, N):
        start_team.append(i)
        dfs(start_team, i+1, cnt+1)
        start_team.pop(-1)
        
dfs([], 0, 0)
print(ans)

"""
아래는 combinations를 활용하여 해결

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
"""