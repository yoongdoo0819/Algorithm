# N과 M (12) (BOJ 15666)

from collections import defaultdict

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

result = []
result_maps = defaultdict()

def dfs(idx):
    
    if len(result) == m:
        result_str = ' '.join(map(str, result))
        if not result_str in result_maps:
            result_maps[result_str] = 1
            print(result_str)
        return
    
    for i in range(idx, n):
        val = s[i]
        result.append(val)
        dfs(i)
        result.pop()
            
dfs(0)