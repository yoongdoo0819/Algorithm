def solution(s):

    s = list(s)
    newStr = []
    newStr.append(s[0])
    
    for idx in range(1, len(s)):
        if not newStr:
            newStr.append(s[idx])
        elif newStr[-1] != s[idx]:
            newStr.append(s[idx])
        elif newStr[-1] == s[idx]:
            newStr.pop()
    
    if not newStr:
        return 1
    else:
        return 0
    
    """
    lenStr = len(s)
    s = list(s)
    while s:
        
        for idx in range(0, len(s)-1):
            if s[idx:idx+1] == s[idx+1:idx+2]:
                if idx <= 0:
                    del s[0:2]
                elif idx+2 >= len(s):
                    del s[idx:idx+2]
                else:
                    del s[idx:idx+2]
                #print(">>", s)
                break
                
        if lenStr == len(s):
            return 0
        elif lenStr > len(s):
            lenStr = len(s)
    """