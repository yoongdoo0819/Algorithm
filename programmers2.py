# 타겟 넘버

"""
# 방법 1
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    s = list(map(sum, product(*l)))
    print(s)
    return s.count(target)
"""

"""
# 방법 2
cnt = 0
def dfs(numbers, idx, sum_val, target):
    global cnt 
    
    if idx >= len(numbers):
        if sum_val == target:
            cnt += 1
        return
    
    dfs(numbers, idx+1, sum_val+numbers[idx], target)
    dfs(numbers, idx+1, sum_val-numbers[idx], target)
    
def solution(numbers, target):
    
    dfs(numbers, 0, 0, target)
    return cnt
"""

# 방법 3
from collections import deque
def solution(numbers, target):
    cnt = 0
    q = deque()
    q.append((+numbers[0], 1))
    q.append((-numbers[0], 1))
    
    while q:
        val, idx = q.popleft()
        if idx >= len(numbers):
            if val == target:
                cnt += 1
        else:
            q.append((val+numbers[idx], idx+1))
            q.append((val-numbers[idx], idx+1))
            
    return cnt