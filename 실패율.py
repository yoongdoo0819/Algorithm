def solution(N, stages):
    answer = []
    cnt, failCheck = 0, 0
    userCnt = len(stages)
    
    for stageNum in range(1, N+1):
        
        for stage in stages:
            if stage > stageNum:
                cnt += 1
            if stage >= stageNum:
                failCheck = 1
                
        if cnt == 0 and failCheck == 0:
            failRatio = 0
        elif cnt == 0 and failCheck == 1:
            failRatio = 1
        elif cnt >= 1: 
            failRatio = (userCnt-cnt)/userCnt
            userCnt = cnt
        
        answer.append([failRatio, stageNum])
        cnt = 0
        failCheck = 0
    
    answer.sort(key = lambda x:x[0], reverse=True)
    result = []
    for ans in answer:
        result.append(ans[1])
        
    return result