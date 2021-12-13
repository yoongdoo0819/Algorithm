# N과 M (1) (BOJ 15649)

""" 
# 해결 방안 1

from itertools import permutations
n, m = map(int, input().split())

permutation_list = []
for i in range(1, n+1):
    permutation_list.append(i)
    
for val in permutations(permutation_list, m):
    for i in range(m):
        print(val[i], end =' ')
    print("")
"""

""" 해결 방안 2 """
n, m = map(int, input().split())
s = []

def dfs():
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if not i in s:
            s.append(i)
            dfs()
            s.pop()

dfs()