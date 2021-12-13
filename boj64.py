# N과 M (5) (BOJ 15654)

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
result = []

def dfs():
    
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for val in s:
        if not val in result:
            result.append(val)
            dfs()
            result.pop()
            
dfs()