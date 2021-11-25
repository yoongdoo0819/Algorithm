# 괄호 회전하기

def correct_bracket(brackets):
    stack = []
    
    for element in brackets:
        if element == '[' or element == '(' or element == '{':
            stack.append(element)
        elif element == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False
        elif element == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
        elif element == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop(-1)
            else:
                return False
        
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    
    answer = 0
    brackets = list(s)
    for _ in range(len(s)):
        
        if correct_bracket(brackets) == True:
            answer += 1
        brackets.append(brackets.pop(0))
        
    return answer