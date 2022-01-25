# Four Squares (BOJ 17626)

from math import sqrt
n = int(input())

def find_four_squares():
    square_root = sqrt(n) # sqrt(n) == (n ** 0.5)
    # if n == a * a:
    #     return 1
    if sqrt(n).is_integer():
        return 1
    
    for i in range(1, int(square_root)+1):
        if i**2 > n:
            break
        if sqrt(n-i**2).is_integer():
            return 2
    for i in range(1, int(square_root)+1):
        if i**2 > n:
            break
        for j in range(1, int(sqrt(n-i**2))+1):
            if i**2 + j**2 > n:
                break
            #if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                # print(i ** 2 - j ** 2)
                # print(n**0.5)
                # print((n - i ** 2))
                # print((n - i ** 2 - j ** 2))
                # print((n - i ** 2 - j ** 2) ** 0.5)
                #return 3
            if (sqrt(n-(i**2 + j**2))).is_integer():
                #print((n-(i**2 + j**2)**0.5))
                return 3
            
    return 4

print(find_four_squares())

"""
아래 코드는 시간과 메모리가 충분하다면 동작할런지 ?

from math import sqrt
import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())

ans = 1e9
def dfs(sum, cnt):
    global ans
    
    if sum == N:
        ans = min(ans, cnt)
        return
    elif sum > N:
        return
    
    for i in range(1, int(sqrt(N)+1)):
        dfs(sum + (i ** 2), cnt + 1)
        
dfs(0, 0)
print(ans)

"""