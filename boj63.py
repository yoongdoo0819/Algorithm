# N과 M (4) (BOJ 15652)

n, m = map(int, input().split())
s = []


def dfs(start):
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for val in range(start, n+1):
        s.append(val)
        dfs(val)
        s.pop()
        
dfs(1)