# 기능개발

import math

def solution(progresses, speeds):
    answer = []
    
    left_days_list = []
    for idx, progress in enumerate(progresses):
        left_progress = 100 - progress
        left_days = math.ceil(left_progress/speeds[idx])
        left_days_list.append(left_days)
        
    max_val = left_days_list[0]
    cnt = 1
    for idx in range(1, len(left_days_list)):
        if max_val < left_days_list[idx]:
            answer.append(cnt)
            cnt = 1
            max_val = left_days_list[idx]
        else:
            cnt += 1
            
    answer.append(cnt)
    return answer