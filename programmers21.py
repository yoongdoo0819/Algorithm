# 수식 최대화

from itertools import permutations
import re

# 문제풀이 https://www.youtube.com/watch?v=5UPS-lvZL2g
def solution(expression):
    operators = list(permutations(['+', '-', '*'], 3))
    expression = re.split('([-+*])', expression)
    result = []
    
    for operator in operators:
        
        exp = expression[:]
        for op in operator:
            
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + exp[idx] + exp[idx+1]))
                del exp[idx:idx+2]
        
        result.append(abs(int(exp[0])))
    
    return max(result)