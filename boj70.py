# N과 M (11) (BOJ 15665)

from collections import defaultdict

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

result = []
num_of_int_maps = defaultdict()
result_maps = defaultdict()


def dfs():
    
    if len(result) == m:
        result_str = ' '.join(map(str, result))
        if not result_str in result_maps:
            result_maps[result_str] = 1
            print(result_str)
        return
    
    for val in s:
        result.append(val)
        dfs()
        result.pop()
            
dfs()
    
    