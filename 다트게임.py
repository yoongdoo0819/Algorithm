def solution(dartResult):
    answer = 0
    prevScore, currScore = 0, 0
    idx = 0
    
    while idx < len(dartResult):
        
        dartScore = dartResult[idx]
        
        if dartScore.isdigit():
            
            answer += prevScore
            prevScore = currScore
                
            if dartResult[idx+1].isdigit():
                currScore = int(dartScore + dartResult[idx+1])
                idx += 2
                continue
            else :
                currScore = int(dartScore)
                
        #elif dartScore == 'S':
        #    currScore = currScore
        elif dartScore == 'D':
            currScore = currScore**2
        elif dartScore == 'T':
            currScore = currScore**3
        elif dartScore == '*':
            prevScore = prevScore * 2
            currScore = currScore * 2
        elif dartScore == '#':
            currScore = -1 * currScore
        
        idx += 1
    
    return answer + prevScore + currScore