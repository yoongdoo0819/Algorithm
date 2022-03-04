# 치킨치킨치킨 (BOJ 16439)

n, m = map(int, input().split())

satisfaction_score = []

for _ in range(n):
    satisfaction_score.append(list(map(int, input().split())))
    
    
score = [0, 0, 0]
answer = 0
def dfs(level):
    global answer
    
    if level == 3:

        sum_val = 0
        for i in range(n):
            
            max_val = 0
            for j in range(3):
                # 선택한 3개의 치킨 중 선호도가 가장 높은 치킨의 만족도를 선택
                max_val = max(max_val, satisfaction_score[i][score[j]])

            sum_val += max_val
            
        answer = max(answer, sum_val)
        return
    
    for pos in range(m):
        score[level] = pos # m개의 치킨 중 치킨 선택하기
        dfs(level+1) # level은 선택한 치킨의 개수를 의미. 즉 총 3개의 치킨 선택 가능
        
dfs(0)
print(answer)

"""
위 코드 중 31~33 line을 아래 코드처럼 수정 가능

N, M = map(int, input().split())
graphs = []

for _ in range(N):
    graphs.append(list(map(int, input().split())))
    
sum = 0
def dfs(idx, depth):
    global sum
    
    if depth == 3:
        temp_sum = 0
        for i in range(N):
            max_val = 0
            for j in idx:
                max_val = max(max_val, graphs[i][j])
            temp_sum += max_val
        
        sum = max(sum, temp_sum)
        return
    
    for i in range(M):
        idx.append(i)
        dfs(idx, depth + 1)
        idx.pop(-1)
        
dfs([], 0)
print(sum)
"""

"""
아래 코드는 combinations를 활용하여 재귀를 사용하지 않고 해결

from itertools import combinations

N, M = map(int, input().split())
chicken_preferences = []

for _ in range(N):
    chicken_preferences.append(list(map(int, input().split())))
    
ans = 0
# 3개의 선호도 (인덱스)를 combinations로 추출하여, 
# 각 사용자는 추출된 선호도 중 가장 높은 선호도의 치킨을 선택
for preference in combinations([i for i in range(M)], 3):
    
    sum_val = 0
    for i in range(N):
        max_val = 0
        for j in range(3):
            max_val = max(max_val, chicken_preferences[i][preference[j]])
        sum_val += max_val
    ans = max(ans, sum_val)
  
print(ans)

"""