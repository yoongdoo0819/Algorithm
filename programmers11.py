# 124 나라의 숫자

def solution(n):
    answer = []
    
    while n > 0:
        quotient = n // 3
        remainder = n % 3
        if remainder == 0:
            quotient -= 1
            if quotient == 0:
                remainder = n
                
            else:
                remainder = n - (3 * quotient)
            if remainder == 3:
                remainder = 4
                
        n = quotient
        answer.append(str(remainder))
    
    return "".join(answer[::-1])