# 숨바꼭질 3 (못품)

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
min_val = 10000000
def dfs(n, count):

    global min_val
    global idx
    
    if n < 0 or n > 100000:
        return 
    
    elif n > k:
        dfs(n-1, count+1)
        
    elif n == k:
        min_val = min(min_val, count)
        
    elif n < k:
        dfs(n+1, count+1)
        dfs(n*2, count)
        """
        n이 k보다 작을 때도 dfs를 돌려야 최솟값을 찾을 수 있는데,
        +와 -가 호출되면 n의 값이 변동이 없으므로 재귀를 계속 반복하는 듯 보임.
        dfs(n-1, count+1) 
        """
        
dfs(n, 0)
print(">>", min_val)