# 가장 큰 수

from functools import cmp_to_key

def xy_compare(x, y):
    return int(y+x) - int(x+y)
    
def solution(numbers):
    
    if max(numbers) == 0:
        return "0"
    
    str_num = list(map(str, numbers))
    str_num.sort(key=cmp_to_key(xy_compare))
    
    return ''.join(str_num)