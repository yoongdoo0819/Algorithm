# 예산 (BOJ 2512)

"""
나무 자르기 (BOJ 2805) 
랜선 자르기 (BOJ 1654)
위 문제들과 비슷한 유형.

"""

N = int(input())
req_arr = list(map(int, input().split()))
M = int(input())

s, e = 1, max(req_arr)

while s <= e:
    mid = (s + e) // 2
    
    sum = 0
    for req in req_arr:
        if req >= mid:
            sum += mid
        else:
            sum += req
            
    if sum > M:
        e = mid - 1
    else:
        s = mid + 1
        
print(e)