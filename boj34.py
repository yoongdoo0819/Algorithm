# 텀 프로젝트 (BOJ 9466)

"""
시간초과 발생
"""
    
t = int(input())
n = []
std_num = []
for j in range(t):
    n.append(int(input()))
    std_num.append(list(map(int, input().split())))
    
        
def dfs(init_std, std, visited):
    global std_set
    
    for next in num_term_projects[std]:
        if not next in visited:
            visited.add(next)
            dfs(init_std, next, visited)
            visited.remove(next)      
        else:
            if init_std == next:
                std_set = std_set | visited  
    
    
visited = set()
for j in range(t):
    std_set = set()
    num_term_projects = [ [] for _ in range(n[j]+1) ]
    
    for i in range(1, n[j]+1):
        num_term_projects[std_num[j][i-1]].append(i)
        
    for i in range(1, n[j]+1):
        
        visited.add(i)
        dfs(i, i, visited)
        visited.remove(i)
        
    print(len(num_term_projects)-len(std_set)-1)
    #result.append(len(num_term_projects)-len(std_set)-1)
    