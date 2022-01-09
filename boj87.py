# 숫자 야구 (BOJ 2503)

from itertools import permutations

n = int(input())

num_baseball_list = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    
    candidate_answer, target_strike_cnt, target_ball_cnt = input().split()
    target_strike_cnt = int(target_strike_cnt)
    target_ball_cnt = int(target_ball_cnt)
        
    for num_baseball_idx, num_baseball in enumerate(num_baseball_list):

        if num_baseball == 'X':
            continue
                
        curr_strike_cnt, curr_ball_cnt = 0, 0
        for num_idx in range(3):
            if int(candidate_answer[num_idx]) == num_baseball[num_idx]:
                curr_strike_cnt += 1
            elif int(candidate_answer[num_idx]) in num_baseball:
                curr_ball_cnt += 1
                
        if curr_strike_cnt != target_strike_cnt or curr_ball_cnt != target_ball_cnt:
            num_baseball_list[num_baseball_idx] = 'X'
            

answer = 0
for num_baseball in enumerate(num_baseball_list):
    if num_baseball[1] != 'X':
        answer += 1
        
print(answer)