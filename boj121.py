# 랜선 자르기 (BOJ 1654)

"""
나무 자르기 (BOJ 2805) 문제와 비슷한 유형.

"""

K, N = map(int, input().split())
lan_arr = []

for _ in range(K):
    lan_arr.append(int(input()))
    
s, e = 1, max(lan_arr)

while s <= e:
    mid = (s + e) // 2
    
    cnt = 0
    for lan in lan_arr:
        cnt += lan // mid
        
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1 
        
print(e)