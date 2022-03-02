# N과 M (3) (BOJ 15651)

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
s = []


def dfs():
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
        
    for idx in range(1, n+1):
        s.append(idx)
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
        res.append(i)
        dfs(res, cnt + 1)
        res.pop(-1)

res = []        
for i in range(1, N+1):
    res.append(i)
    dfs(res, 1)
    res.pop(-1)

"""