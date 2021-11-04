def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    strList1, strList2 = [], []
    strDict = dict()
    strDict2 = dict()
    
    for i in range(0, len(str1)-1):
        if str1[i:i+1].islower() == True and str1[i+1:i+2].islower() == True:
            strList1.append(str1[i:i+2])
            strDict[str1[i:i+2]] = 0
    for i in range(0, len(str2)-1):
        if str2[i:i+1].islower() == True and str2[i+1:i+2].islower() == True:
            strList2.append(str2[i:i+2])
            strDict2[str2[i:i+2]] = 0
    
    for idx, v in enumerate(strList1):
        strDict[v] += 1
    for idx, v in enumerate(strList2):
        strDict2[v] += 1
    
    sum = 0
    setStr = list(set(strList1) | set(strList2))
    for idx, val in enumerate(setStr):
        if val in strDict and val in strDict2:
            num1 = strDict[val]
            num2 = strDict2[val]
            minNum = min(num1, num2)
            sum += minNum
    
    #print(sum)
    unionNum = len(strList1) + len(strList2) - sum
    if len(strList1) + len(strList2) == 0:
        return 65536
    
    return int((sum/unionNum)*65536)