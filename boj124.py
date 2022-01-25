# 입국심사 (BOJ 3079)

import sys

N, M = map(int, input().split())
time_arr = []
for _ in range(N):
    time_arr.append(int(input()))

left = min(time_arr)
answer = right = max(time_arr) * M

while left <= right:
    
    mid = (left + right) // 2
    total = 0
    for i in range(N):
        total += mid // time_arr[i]
    if total >= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)

"""
아래 코드는 메모리 초과
import sys

N, M = map(int, sys.stdin.readline().split())
time_arr = []
waiting_list = []

for _ in range(N):
    time_arr.append(sys.stdin.readline())

for time in time_arr:
    temp = time
    waiting_list.append(temp)
    while temp <= max(time_arr)*M:
        temp += time
        waiting_list.append(temp)
        
waiting_list.sort()
#print(waiting_list)
print(waiting_list[M-1])

"""