# 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
datas = list(map(int, input().split()))
cnt = 0

for data in combinations(datas, 2):
    print(data)
    if data[0] != data[1]:
        cnt += 1
    
print(cnt)
"""
# book answer
array = [0] * 11
for x in datas:
    array[x] += 1
    
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
    
print(result)
"""