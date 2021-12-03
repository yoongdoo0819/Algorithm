# 샘터

from collections import deque

n, k = map(int, input().split())
sam_list = list(map(int, input().split()))
q = deque()
"""
visited = []로 초기화 이후, 
visited.append()로 코드를 수정하면 시간초과 발생. 
visited = set() 초기화 이후, visited.add()는 시간 내에 통과
set() 연산이 더 속도가 빠른듯. 왜?
"""
visited = set()

for sam in sam_list:
    q.append((sam, 0))
    visited.add(sam)
    
num_of_house = 0
total_dist = 0
def bfs():
    global num_of_house
    global total_dist
    
    while q:
        sam, dist = q.popleft()
    
        for next in [1, -1]:
            if sam+next in visited:
                continue
            else:
                q.append((sam+next, dist+1))    
                num_of_house += 1
                total_dist += dist + 1
                visited.add(sam+next)
                if num_of_house == k:
                    print(total_dist)
                    return

bfs()