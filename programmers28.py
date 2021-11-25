# 최댓값과 최솟값

def solution(s):
    
    num = s.split()
    intList = list(map(int, num))
    answer = str(min(intList)) + ' ' + str(max(intList))
    
    return answer