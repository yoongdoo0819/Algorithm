# 부분수열의 합 (BOJ 1182)

import sys
sys.setrecursionlimit(10**6)

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = []
cnt = 0
def dfs(start, result):
    global cnt
    
    print(result)
    if sum(result) == s and len(result) > 0:
        cnt += 1
        return
    
    for i in range(start, n):
        val = data[i]
        result.append(val)
        dfs(i+1, result)
        result.pop()

dfs(0, result)
print(cnt)

"""
다시 짠 코드

N, M = map(int, input().split())
datas = list(map(int, input().split()))
ans = 0

def dfs(start, res, cnt):
    global ans
    
    if sum(res) == M and len(res) > 0:
        #print(">>", res)
        ans += 1

    # 아래 if문은 없어도 정답처리 됨.
    if cnt >= N:
        return
    
    for i in range(start, N):
        data = datas[i]
        res.append(data)
        dfs(i+1, res, cnt + 1)
        res.pop(-1)

dfs(0, [], 0)
print(ans)

"""