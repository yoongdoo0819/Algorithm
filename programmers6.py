# N개의 최소공배수

def gcd_func(a, b):
    if b == 0:
        return a
    
    return gcd_func(b, a%b)

def solution(arr):
    
    while len(arr) >= 2:
        num1 = arr.pop(0)
        num2 = arr.pop(0)
        
        gcd = gcd_func(num1, num2)
        lcm = (num1*num2) // gcd
        arr.append(lcm)
        
    return arr[0]