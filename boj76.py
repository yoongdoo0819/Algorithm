# 연산자 끼워넣기 (BOJ 14888)

n = int(input())
num_of_int = list(map(int, input().split()))
num_of_op = list(map(int, input().split()))

min_val = 1e9
max_val = -1e9

def dfs(idx, sum):
    global min_val
    global max_val
    
    if idx == n:
        min_val = min(min_val, sum)
        max_val = max(max_val, sum)
        
    if 0 < num_of_op[0]:
        num_of_op[0] -= 1
        dfs(idx+1, sum+num_of_int[idx])
        num_of_op[0] += 1
        
    
    if 0 < num_of_op[1]:
        num_of_op[1] -= 1
        dfs(idx+1, sum-num_of_int[idx])
        num_of_op[1] += 1
        
    
    if 0 < num_of_op[2]:
        num_of_op[2] -= 1
        dfs(idx+1, sum*num_of_int[idx])
        num_of_op[2] += 1
        
    
    if 0 < num_of_op[3]:
        num_of_op[3] -= 1
        dfs(idx+1, int(sum/num_of_int[idx]))
        num_of_op[3] += 1
        

dfs(1, num_of_int[0])
print(max_val)
print(min_val)