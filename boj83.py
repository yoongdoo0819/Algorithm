# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 (BOJ 2422)

"""
아래 코드는 시간 초과

from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
not_mix_cream_list = []
cream_list = [i for i in range(1, n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    not_mix_cream_list.append([a, b])
    
cnt = 0
for mix_cream_list in combinations(cream_list, 3):
    
    check = True
    for not_mix_cream in not_mix_cream_list:
        if not_mix_cream[0] in mix_cream_list and not_mix_cream[1] in mix_cream_list:
            check = False
            break
        
    if check == True:
        cnt += 1
        
print(cnt)
"""

from itertools import combinations

n, m = map(int, input().split())
not_mix_cream_list = []
cream_list = [i for i in range(1, n+1)]
impossible_mix_cream = [ [ False for _ in range(n+1) ] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    impossible_mix_cream[a][b] = True
    impossible_mix_cream[b][a] = True
    
cnt = 0
for mix_cream_list in combinations(cream_list, 3):
    if impossible_mix_cream[mix_cream_list[0]][mix_cream_list[1]] or impossible_mix_cream[mix_cream_list[0]][mix_cream_list[2]] or impossible_mix_cream[mix_cream_list[1]][mix_cream_list[2]]:
                continue 
            
    cnt += 1
        
print(cnt)