# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while scoville[0] < K:
        
        if len(scoville) == 1:
            break
            
        if len(scoville) >= 2:
            first_food = heapq.heappop(scoville)
            second_food = heapq.heappop(scoville)
            
            new_scoville = first_food + (second_food * 2)
            heapq.heappush(scoville, new_scoville)
            
            answer += 1
    
    if scoville[0] < K:
        return -1
    else:
        return answer