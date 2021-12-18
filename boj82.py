# 가르침 (BOJ 1062)

"""
아래는 구글링 코드
"""
import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)

"""
아래 코드는 시간 초과 발생

import sys
n, k = map(int, input().split())

str_list = []
for _ in range(n):
    str_list.append(sys.stdin.readline().rstrip())

char_list = {}
for i in range(97, 123):
    char_list[chr(i)] = 0
    
for char in ['a', 'c', 'i', 'n', 't']:
    char_list[char] = 1

answer = 0
def dfs(idx, cnt, k):
    global answer
    
    if k-5 == cnt:
        read_cnt = 0
        for str in str_list:
            check = True
            for k, v in char_list.items():
                if k in str and v == 0:
                    check = False
            if check == True:
                read_cnt += 1
                
        answer = max(answer, read_cnt)
        return
    
    for i in range(idx, 26):
        ch = chr(97+i)
        if char_list[ch] == 0:
            char_list[ch] = 1
            dfs(i, cnt+1, k)
            char_list[ch] = 0

if k < 5:
    print(0)
    exit()
    
elif k == 26:
    print(n)
    exit()
    
dfs(0, 0, k)
print(answer)
"""