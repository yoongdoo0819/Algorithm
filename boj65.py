# N과 M (6) (BOJ 15655)

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
        dfs(i+1)
        result.pop()


dfs(0)

"""
직접 짠 코드

N, M = map(int, input().split())
datas = list(map(int, input().split()))
datas.sort()

def dfs(start, res, cnt):
    
    if cnt == M:
        for i in res:
            print(i, end=" ")
        print("")
        return
    
    for i in range(start, len(datas)):
        data = datas[i]
        if not data in res:
            res.append(data)
            dfs(i, res, cnt + 1)
            res.pop(-1)

dfs(0, [], 0)

"""