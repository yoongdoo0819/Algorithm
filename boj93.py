# 스타트와 링크 (BOJ 14889)

"""
dfs로 해결

"""
N = int(input())
teams = []
ans = 1e9

for _ in range(N):
    teams.append(list(map(int, input().split())))

def dfs(start_team, idx, cnt):
    global ans
    
    if cnt == N//2:
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
        return
        
    for i in range(idx, N):
        start_team.append(i)
        dfs(start_team, i+1, cnt+1)
        start_team.pop(-1)
        
dfs([], 0, 0)
print(ans)

"""
아래 코드들은 combinations을 활용하여 해결한 두 가지 방안
(코드는 약간 다름)


첫 번째 해결 코드. 
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


두 번째 해결 코드.
from itertools import combinations

N = int(input())
teams = []
ans = 1e9

for _ in range(N):
    teams.append(list(map(int, input().split())))
    
teams_set = set()
for i in range(N):
    teams_set.add(i)

for team in combinations([i for i in range(N)], N//2):
    start_team_ability = 0
    for i in team:
        for j in team:
            start_team_ability += teams[i][j]
        
    link_team_ability = 0
    link_team = [i for i in range(N)]
    for idx in team:
        link_team.remove(idx)
    
    for i in link_team:
        for j in link_team:
            link_team_ability += teams[i][j]
        
    ans = min(ans, abs(start_team_ability-link_team_ability))
    
print(ans)

"""