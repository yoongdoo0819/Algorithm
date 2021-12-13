# N과 M (2) (BOJ 15650)

"""
# 해결 방안 1
from itertools import combinations

n, m = map(int, input().split())

data = []
for idx in range(1, n+1):
    data.append(idx)
    
for comb_list in combinations(data, m):
    for val in comb_list:
        print(val, end = ' ')
    print("")
"""

""" 해결 방안 2 """
n, m = map(int, input().split())
s = []

def dfs(i):
    
    #print("curr", s, i)
    if len(s) == m:
        print(' '.join(map(str, s)))
        #print("exit", i)
        return
    else:
        for val in range(i, n+1):
            if not val in s:
                #print("add", val, " before ", val+1)
                s.append(val)
                dfs(val+1)
                s.pop()
                #print("pop", val, " after", val+1)
dfs(1)