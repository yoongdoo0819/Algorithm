# 연산 최대로 (BOJ 21943)

from itertools import combinations

N = int(input())
num_list = list(map(int, input().split()))
P, M = map(int, input().split())

ans = 0

def dfs(curr_val, cnt, temp_list):
    global ans
    
    if cnt == 0:
        # 맨 처음 시작 시 사용 가능한 곱셈 개수가 2개라면 (cnt = 2), 
        # 46 line에서 dfs를 처음 재귀적으로 들어갈 때 감소하는 cnt-1은, 실제 곱셈을 한 것은 아님.
        # 왜냐하면 48 line에서 맨 처음 dfs를 호출할 때 curr_val을 1로 설정하기 때문에, 단순 재귀적으로 표현하기 위한 것.
        
        # 따라서, 맨 처음 시작 시 cnt = 2라면, 
        # cnt가 1일때 실제 곱셈 연산을 한 번 수행하며,
        # cnt가 0일때 실제 곱셈 연산을 한 번 더 수행함. 
        ans = max(ans, curr_val*sum(temp_list))
        return
    
    # idx_list = range(len(temp_list)) 코드와 동일
    idx_list = [ i for i in range(len(temp_list)) ]  

    # 1부터 숫자 리스트의 총 개수까지, 현재 사용 가능한 곱셈의 개수를 제외하여 반복
    # 예를 들어, 만약 temp_list가 6개의 숫자(1, 2, 4, 5, 7, 8)를 포함하고 있으며, 
    # 가능한 곱셈의 수가 2개라면,
    # 1 x 2 x (4+5+7+8) / (1+2+4+5) x 7 x 8 등과 같이 식을 구성할 수 있음.
    for pick_cnt in range(1, len(temp_list)+1 - cnt):
        for comb in combinations(idx_list, pick_cnt):
            copy_temp_list = temp_list[:]
            
            # reversed(comb)를 안해주면, 아래 코드에서 copy_temp_list.pop(idx) 연산 시
            # comb는 오름차순으로 정렬되어 있기 때문에, 작은 값의 idx부터 pop 연산을 수행하게 됨.
            # 그렇게 copy_temp_list를 pop하면, pop한 자리를 채우기 위해 오른쪽 값들이 모두 왼쪽으로 채워지며,
            # 실제 copy_temp_list에서 값을 삭제할 인덱스를 나타내는 comb와 불일치하게 됨.
            # 예를 들어, copy_temp_list = [5, 4]이고, comb = [0, 1]인 경우, copy_temp_list에서 먼저 0번째 인덱스인 5를 제거하고,
            # 그 다음 1번째 인덱스인 4를 제거해야 하지만, 이미 5를 제거하였으므로 copy_temp_list의 인덱스 범위를 초과해버림. 
            comb = list(reversed(comb))
            temp_sum = 0
            for idx in comb:
                temp_sum += copy_temp_list.pop(idx)
            dfs(curr_val*temp_sum, cnt-1, copy_temp_list)

dfs(1, M, num_list)
print(ans)