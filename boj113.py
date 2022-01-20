# 블로그2 (BOJ 20365)

"""
아래 코드는 구글링
"""

import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
cnt = {'B': 0,'R': 0}
cnt[s[0]] += 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cnt[s[i]] += 1
        
print(min(cnt['B'],cnt['R'])+1)


"""
아래와 같은 코드가 틀리는 이유는,
RBRBBBR이 주어졌을 때, 
먼저 R로 1번 모두 색칠 후, 연속된 B를 2번 색칠하면 총 3번의 작업이 걸림.
그러나, B로 1번 모두 색칠 후 R을 3번 색칠하면 (연속된 R이 없으므로) 총 4번의 작업이 걸림.
아래 코드는 count() 함수를 사용하여, B와 R 중 더 적은 갯수가 무엇인지 판별하여, 더 적은 갯수에 대해 색칠하려 하지만,
중요한 것은 B와 R의 갯수가 아님.
갯수가 많더라도 연속하여 색칠할 수 있느냐 마느냐가 중요 
(갯수가 많더라도 많은 부분을 연속하여 색칠할 수 있으면 더 적은 작업량이 요구되기 때문)

n = int(input())
s = input()
blue_cnt, red_cnt = s.count('B'), s.count('R')
total_cnt = 0


TARGET_COLOR = ''
if blue_cnt >= red_cnt:
    TARGET_COLOR = 'R'
elif blue_cnt < red_cnt:
    TARGET_COLOR = 'B'

check = False
for i in range(len(s)):
    color = s[i]
    
    if check == False and color == TARGET_COLOR:
        check = True
    elif check == False and color != TARGET_COLOR:
        continue
    elif check == True and color == TARGET_COLOR:
        continue
    elif check == True and color != TARGET_COLOR:
        total_cnt += 1
        check = False

if check == True:
    total_cnt += 1
    
print(total_cnt+1)
"""