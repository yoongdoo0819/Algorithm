# 종이 조각 (BOJ 14391)

"""
비트마스크 문제.
구글링 참고함.
"""

from itertools import product

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
    
def to_matrix(l, m):
    #print(l, len(l), l[0:0+m])
    return [ l[i:i+m] for i in range(0, len(l), m) ]

a = list(product([0, 1], repeat=N*M))
ans = 0

for x in a:
    
    # 1. 발생할 수 있는 모든 경우의 수 (0과 1로 구성된) 에서,
    bit_mask = to_matrix(x, M)
    
    
    # 2. 0과 1 구성 요소에 따라 
    # (0을 만나면 입력으로 받았던 실제 값을 자릿수를 옮겨가며 저장,
    #  1을 만나면 sum_col 변수에 누적하여 저장하는 방식),
     
    # 가로 (column)로 계산한 값과
    sum_col = 0
    for i in range(N):
        temp_col = 0
        for j in range(M):
            if bit_mask[i][j] == 0:
                temp_col = 10 * temp_col + graph[i][j]
            if bit_mask[i][j] == 1 or j == M-1:
                sum_col += temp_col
                temp_col = 0

    # 3. 세로 (row)로 계산한 값을 더해서, 가장 큰 값을 ans에 담음
    sum_row = 0
    for j in range(M):
        temp_row = 0
        for i in range(N):
            if bit_mask[i][j] == 1:
                temp_row = 10 * temp_row + graph[i][j]
            if bit_mask[i][j] == 0 or i == N-1:
                sum_row += temp_row
                temp_row = 0
        
    ans = max(ans, sum_col+sum_row)

print(ans)