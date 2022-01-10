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