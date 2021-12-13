# N과 M (7) (BOJ 15656)

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

result = []

def dfs():
    
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for val in s:
        result.append(val)
        dfs()
        result.pop()
        
dfs()