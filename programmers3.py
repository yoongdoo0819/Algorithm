# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    
    for idx, number in enumerate(numbers):
        if numbers[idx] == 0:
            numbers[idx] = 11
            
    pad = [
        0, # empty
        (1, 1), (1, 2), (1, 3), # 1,    2,    3
        (2, 1), (2, 2), (2, 3), # 4,    5,    6
        (3, 1), (3, 2), (3, 3), # 7,    8,    9
        (4, 1), (4, 2), (4, 3), # *,  11(0),  #
    ]
    leftNum = [1, 4, 7]
    rightNum = [3, 6, 9]
    middleNum = [2, 5, 8, 11]
    leftPos, rightPos = 10, 12
        
    for number in numbers:
        
        if number in leftNum:
            answer += 'L'
            leftPos = number
        
        elif number in rightNum:
            answer += 'R'
            rightPos = number
            
        elif number in middleNum:
            leftX, leftY = pad[leftPos]
            rightX, rightY = pad[rightPos]
            numX, numY = pad[number]
            leftDist = abs(leftX - numX) + abs(leftY - numY) 
            rightDist = abs(rightX - numX) + abs(rightY - numY)
            
            if leftDist == rightDist:
                if hand == 'left':
                    answer += 'L'
                    leftPos = number
                elif hand == 'right':
                    answer += 'R'
                    rightPos = number
            elif leftDist < rightDist:
                answer += 'L'
                leftPos = number
            elif rightDist < leftDist:
                answer += 'R'
                rightPos = number
            
    return answer