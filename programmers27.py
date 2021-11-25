# 다리를 지나는 트럭

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