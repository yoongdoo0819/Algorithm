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

"""
직접 짠 코드

N, M = map(int, input().split())

def dfs(res, cnt):
    
    if cnt == M:
        for i in res:
            print(i, end=" ")
        print("")
        return
    
    for i in range(1, N+1):
        if not i in res:
            res.append(i)
            dfs(res, cnt + 1)
            res.pop(-1)
    
res = []        
for i in range(1, N+1):
    res.append(i)
    dfs(res, 1)
    res.pop(-1)

"""