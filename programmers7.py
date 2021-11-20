# 괄호 변환

def correct_str(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

def balanced_str(s):
    cnt = 0
    for idx, ch in enumerate(s):
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
        if cnt == 0:
            return s[:idx+1], s[idx+1:]

def reverse_str(s):
    temp_s = ''
    for ch in s:
        if ch == '(':
            temp_s += ')'
        else:
            temp_s += '('
            
    return temp_s
    
def solution(p):
    u = ''
    
    if len(p) == 0:
        return u
    
    u, v = balanced_str(p)
    if correct_str(u) == True:
        u += solution(v)
    else:
        empty_str = '('
        empty_str += solution(v)
        empty_str += ')'
        u = u[1:-1]
        u = empty_str + reverse_str(u)
    
    return u