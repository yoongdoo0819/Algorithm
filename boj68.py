# N과 M (9) (BOJ 15663)

from collections import defaultdict

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

result = []
result_maps = defaultdict(list)
num_of_int_maps = defaultdict(list)

for val in s:
    if not val in num_of_int_maps:
        num_of_int_maps[val] = 1
    else:
        num_of_int_maps[val] += 1
        
def dfs():
    
    if len(result) == m:
        result_str = ' '.join(map(str, result))
        if not result_str in result_maps:
            result_maps[result_str] = 1
            print(result_str)
        return
    
    for i in range(0, n):
        val = s[i]
        if not val in result or (num_of_int_maps[val] > 0):
            num_of_int_maps[val] -= 1
            result.append(val)
            dfs()
            result.pop()
            num_of_int_maps[val] += 1
            
dfs()