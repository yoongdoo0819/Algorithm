# 괄호 추가하기 (BOJ 16637)

from copy import deepcopy

n = int(input())
s = input()

num = []
op = []
for char in s:
    if char.isdigit():
        num.append(char)
    else:
        op.append(char)
        
answer = -1e9 # eval(s)
def dfs(total_sum, idx):
    global answer 
    
    if idx >= len(op):
        answer = max(answer, total_sum)
        return
    
    sequence_sum = eval(str(total_sum) + op[idx] + num[idx+1])
    dfs(sequence_sum, idx + 1)
    
    if idx + 1 < len(op):
        not_sequence_sum = str(eval(num[idx+1] + op[idx+1] + num[idx+2]))
        not_sequence_sum = eval(str(total_sum) + op[idx] + not_sequence_sum)
        dfs(not_sequence_sum, idx + 2)
        
dfs(int(num[0]), 0)
print(answer)