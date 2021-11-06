def solution(s):
    answer = ""
    numToAlphabet = {
        'zero'  :0,
        'one'   :1,
        'two'   :2,
        'three' :3,
        'four'  :4,
        'five'  :5,
        'six'   :6,
        'seven' :7,
        'eight' :8,
        'nine'  :9
    }
    
    voca = ""
    for i in range(0, len(s)):
        
        if not s[i].isdigit():
            voca += s[i]
            if voca in numToAlphabet.keys():
                answer += str(numToAlphabet[voca])
                voca = ""
            
        else: 
            answer += s[i]
        
    
    return int(answer)