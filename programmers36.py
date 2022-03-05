# 프린터

from collections import deque

def solution(priorities, location):
    
    datas = deque()
    idx = 0
    for priority in priorities:
        datas.append((priority, idx))
        idx += 1
            
    cnt = 1
    while True:
        priority, idx = datas.popleft() 
        
        check = True
        for left_priority, _ in datas:
            if priority < left_priority:
                check = False
        if check == False:
            datas.append((priority, idx))
        elif check == True and idx == location:
            return cnt
        elif check == True and idx != location:
            cnt += 1
            
            