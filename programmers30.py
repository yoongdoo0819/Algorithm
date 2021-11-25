# 다음 큰 숫자

def solution(n):
    answer = n + 1
    target_cnt = bin(n).count('1')
    
    while True:
        if bin(answer).count('1') == target_cnt:
            return answer
        else:
            answer += 1
        
    return answer
