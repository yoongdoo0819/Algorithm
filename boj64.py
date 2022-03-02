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

"""
직접 짠 코드


N, M = map(int, input().split())
datas = list(map(int, input().split()))
datas.sort()

def dfs(res, cnt):
    
    if cnt == M:
        for i in res:
            print(i, end=" ")
        print("")
        return
    
    for i in datas:
        if not i in res:
            res.append(i)
            dfs(res, cnt + 1)
            res.pop(-1)

dfs([], 0)

"""