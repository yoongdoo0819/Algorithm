# 예상 대진표

import math

def solution(n,a,b):

    idx = 1
    while idx <= math.ceil(math.sqrt(n)):
    
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        
        if a == b:
            return idx
        
        idx += 1
    
    return idx