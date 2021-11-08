def solution(n, arr1, arr2):
    answer = []
    cryptoArr1, cryptoArr2 = [], []
    
    for arr in arr1:
        binArr = str(bin(arr)[2:])
        diff = n - len(binArr)
        addZero = '0' * diff
        binArr = addZero + binArr
        
        cryptoArr1.append(list(binArr))
        
    for arr in arr2:
        binArr = str(bin(arr)[2:])
        diff = n - len(binArr)
        addZero = '0' * diff
        binArr = addZero + binArr
        
        cryptoArr2.append(list(binArr))
    
    decodeMap = []
    for listIdx in range(0, n):
        
        decodeMapList = ""
        
        for idx in range(0, n):
            if cryptoArr1[listIdx][idx] == '1' or cryptoArr2[listIdx][idx] == '1':
                decodeMapList += '#'
            elif cryptoArr1[listIdx][idx] == '0' or cryptoArr2[listIdx][idx] == '0':
                decodeMapList += ' '
        
        decodeMap.append(decodeMapList)
    
    
    return decodeMap