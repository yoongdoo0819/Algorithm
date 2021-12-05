# 소가 길을 건너간 이유 1 (BOJ 14467)

maps = {}
n = int(input())
for i in range(1, 11):
    maps[i] = -1
    
cnt = 0
for _ in range(n):
    cow_num, loc = map(int, input().split())
    if maps[cow_num] == -1:
        maps[cow_num] = loc
    elif maps[cow_num] != loc:
        cnt += 1
        maps[cow_num] = loc
        
print(cnt)