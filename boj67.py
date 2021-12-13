# N과 M (8) (BOJ 15657)

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

result = []

def dfs(idx):
    
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx, n):
        val = s[i]
        result.append(val)
        dfs(i)
        result.pop()
        
dfs(0)