# 주식가격

def solution(prices):
    answer = []
    
    for idx, price in enumerate(prices):
        
        cnt = 0
        for j in range(idx+1, len(prices)):
            cnt += 1
            if price > prices[j]:
                break
        
        answer.append(cnt)
    
    return answer