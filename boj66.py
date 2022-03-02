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
    
    for i in range(0, len(datas)):
        data = datas[i]
        #if not data in res:
        res.append(data)
        dfs(res, cnt + 1)
        res.pop(-1)

dfs([], 0)

"""