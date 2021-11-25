# JadenCase 문자열 만들기

def solution(s):
    check = 1
    jadenCase = ''
    
    for ch in s:
        
        if ch == ' ':
            jadenCase += ch
            check = 1
        elif ch != ' ' and check == 1:
            jadenCase += ch.upper()
            check = 0
        else:
            jadenCase += ch.lower()
        
    return jadenCase