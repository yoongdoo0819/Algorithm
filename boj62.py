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