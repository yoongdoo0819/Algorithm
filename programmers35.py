# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    hashMap = {}
    
    for party in participant:
        if party not in hashMap:
            hashMap[party] = 1
        else:
            hashMap[party] += 1
            
    for party in completion:
        hashMap[party] -= 1
        
    for k, v in hashMap.items():
        if v == 1:
            answer = k
    
    return answer