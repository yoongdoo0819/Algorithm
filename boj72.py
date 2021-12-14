# 부분수열의 합 (BOJ 1182)

import sys
sys.setrecursionlimit(10**6)

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = []
cnt = 0
def dfs(start, result):
    global cnt
    
    print(result)
    if sum(result) == s and len(result) > 0:
        cnt += 1
        return
    
    for i in range(start, n):
        val = data[i]
        result.append(val)
        dfs(i+1, result)
        result.pop()

dfs(0, result)
print(cnt)