# 이진 변환 반복하기

def solution(s):
    answer = []
    loopCnt, zeroCnt = 0, 0
    
    while len(s) > 1:
        len1 = len(s)
        s = s.replace("0", "")
        len2 = len(s)
        newLen = len1 - len2
        zeroCnt += newLen

        s = bin(len2)[2:]
        
        loopCnt += 1
    
    return [loopCnt, zeroCnt]