# 정수 제곱근 (BOJ 2417)

from sympy import E

n = int(input())
s = 0
e = n

while s < e:
    mid = (s + e) // 2
    if mid ** 2 > n:
        e = mid
    else:
        s = mid + 1

print(s)

"""

import math

n = int(input())
start = int(math.sqrt(n))

for i in range(start, n):
    if i ** 2 >= n:
        print(i)
        exit(0)
        
print(n)

"""