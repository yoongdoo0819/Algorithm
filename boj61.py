# N과 M (2) (BOJ 15650)

from itertools import combinations

n, m = map(int, input().split())

data = []
for idx in range(1, n+1):
    data.append(idx)
    
for comb_list in combinations(data, m):
    for val in comb_list:
        print(val, end = ' ')
    print("")