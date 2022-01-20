# 회의실 배정 (BOJ 1931)

n = int(input())
seminar_room = []

for _ in range(n):
    start_time, end_time = map(int, input().split())
    seminar_room.append((start_time, end_time))
    
"""
2 2
1 2
위와 같은 회의 테이블이 주어진다면,
(1 2) (2 2) 순서로 진행하면 두 개의 회의를 진행할 수 있음
그러나, (2 2) (1 2) 순서로 진행하면 회의를 하나밖에 진행할 수 없음
따라서, 1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순으로 정렬해주어야 함
"""
seminar_room.sort(key=lambda x : (x[1], x[0]))
start_time, end_time = seminar_room[0]
cnt = 1

for i in range(1, n):
    next_start_time, next_end_time = seminar_room[i]
    
    if next_start_time >= end_time:
        start_time, end_time = next_start_time, next_end_time
        cnt += 1
        
print(cnt)