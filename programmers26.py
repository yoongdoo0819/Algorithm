# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for sub_dungeons in permutations(dungeons):
        exhaustion = k
        cnt = 0
        
        for dungeon in sub_dungeons:
            
            need_exhaustion, consume_exhaustion = dungeon
            if exhaustion >= need_exhaustion:
                exhaustion -= consume_exhaustion
                cnt += 1
        answer.append(cnt)
        
    return max(answer)


"""
아래는 dfs 풀이

mx = 0
def dfs(k, dungeons, cnt, visited):
    global mx
    mx = max(mx, cnt)
    
    for i in range(0, len(dungeons)):
        if not visited[i]:
            visited[i] = True
            x, y = dungeons[i]
            if k >= x:
                dfs(k-y, dungeons, cnt+1, visited)
            visited[i] = False

def solution(k, dungeons):
    visited = [False] * (len(dungeons)+1)
    dfs(k, dungeons, 0, visited)
    return mx

"""