# 애너그램 (BOJ 6443)

import sys

n = int(sys.stdin.readline())

def dfs(curr_length, target_length):
    
    if curr_length == target_length:
        sys.stdout.write(''.join(temp_s) + "\n") 
        return
        
    for i in visited:
        if visited[i] > 0:
            visited[i] -= 1
            temp_s[curr_length] = i
            dfs(curr_length+1, target_length)
            visited[i] += 1
                

for _ in range(n):
    s = list(sys.stdin.readline().strip())
    s.sort()
    visited = {}
    for i in range(len(s)):
        if s[i] in visited:
            visited[s[i]] += 1
        else:
            visited[s[i]] = 1
            
    temp_s = [0] * len(s)
    dfs(0, len(s))
    
"""
# 아래처럼 temp_s애서 dfs 이전에 문자열 하나를 append하고, dfs 직후 pop 연산을 통해 append했던 문자열을 제거한다면 시간 초과 발생
# 또한, 중복되는 문자열 출력을 방지하고자 set이나 map을 이용하는 것 역시 시간 초과 발생
# 애너그램 (BOJ 6443)

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dup_set = set() # defaultdict(list)

def dfs(s, temp_s):
        global dup_set
        
        if len(s) == len(temp_s):
            #ans = ''.join(temp_s)
            if not temp_s in dup_set:
                dup_set.add(temp_s)
                print(temp_s)
            return
            
        for i in range(len(s)):
            if not visited[i]:
                visited[i] = True
                #temp_s.append(s[i])
                dfs(s, temp_s+s[i])
                #temp_s.pop()
                visited[i] = False

for _ in range(n):
    s = list(sys.stdin.readline().strip())
    result = []
    visited = [False] * len(s)
    s.sort()
    dfs(s, "")
    
"""