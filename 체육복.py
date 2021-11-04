def solution(n, lost, reserve):
    
    newLost = list(set(lost) - set(reserve))
    newReserve = list(set(reserve) - set(lost))
    answer = n - len(newLost)
    
    for i in range(0, len(newReserve)):
        
        if answer >= n:
            break
            
        for j in range(0, len(newLost)):
            
            if newReserve[i]+1 == newLost[j] or newReserve[i]-1 == newLost[j]:
                answer += 1
                newReserve[i] = -1
                newLost[j] = -1
                break
    
    return answer