# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    q = deque()
    time = 0
    trucks = []
    
    # 대기 트럭 초기화
    for truck in truck_weights:
        trucks.append((truck, 0))
    
    while trucks or q:
        
        # 다리를 건너고 있는 트럭이 있다면 해당 트럭들의 1초 경과 시간을 표시
        for _ in range(len(q)):
            truck, second = q.popleft()
            if second + 1 <= bridge_length:
                q.append((truck, second+1))
            
        # 대기 트럭
        if trucks:
            truck, second = trucks[0]
            
            # 다리를 건너고 있는 트럭의 총 무게 계산
            total_weight = 0
            for passing_truck, _ in q:
                total_weight += passing_truck

            # 건너려는 다리가 (다리를 건너고 있는 트럭의 총 무게 + 대기 트럭에서 새롭게 오르는 트럭) 을 견뎌낼 수 있는지
            if total_weight + truck <= weight:
                q.append((truck, 1))
                trucks.pop(0)
        
        time += 1    
                
    
    return time

"""
풀이방법 두번째.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    queue = deque()
    queue.append([truck_weights[0], 1])
    idx = 1
    cnt = 0
    
    #print (bridge_length, weight, truck_weights)
    while cnt < len(truck_weights):
        
        answer += 1
        if not queue and idx < len(truck_weights):
            queue.append([truck_weights[idx], 1])
            idx += 1
        else:
            total_weight = 0
            for _ in range(len(queue)):
                truck = queue.popleft()
                if truck[1] == bridge_length:
                    cnt += 1
                else:
                    truck[1] += 1
                    total_weight += truck[0]
                    queue.append(truck)
            if idx < len(truck_weights) and total_weight + truck_weights[idx] <= weight :
                queue.append([truck_weights[idx], 1])
                idx += 1
        
    return answer
    
"""