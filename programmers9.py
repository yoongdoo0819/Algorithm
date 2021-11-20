# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    
    n_row = len(arr1)
    n_col = len(arr1[0])
    m_row = len(arr2)
    m_col = len(arr2[0])
    
    for i in range(n_row):
        
        temp_list = []
        for k in range(m_col):
            
            temp_sum = 0
            for j in range(n_col):
                temp_sum += arr1[i][j] * arr2[j][k]
                #print(i, j, arr1[i][j], arr2[j][k])
                
            temp_list.append(temp_sum)
        answer.append(temp_list)
            
    return answer