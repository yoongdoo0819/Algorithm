# 타겟 넘버

cnt = 0

def dfs(numbers, target, depth, num_sum):
    global cnt
    
    if len(numbers) == depth:
        if num_sum == target:
            cnt += 1
        return
    
    dfs(numbers, target, depth+1, num_sum + numbers[depth])
    dfs(numbers, target, depth+1, num_sum - numbers[depth])
    
def solution(numbers, target):
    
    dfs(numbers, target, 0, 0)
    return cnt