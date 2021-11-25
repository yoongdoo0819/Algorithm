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