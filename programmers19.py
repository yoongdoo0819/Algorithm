# 올바른 괄호

def correct_bracket(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    

def solution(s):
    
    return correct_bracket(s)