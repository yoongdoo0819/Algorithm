# 나무 자르기 (BOJ 2805)

N, TARGET = map(int, input().split())
tree_height_arr = list(map(int, input().split()))

s, e = 1, max(tree_height_arr)
ans = 0

while s <= e:
    mid = (s + e) // 2
    
    sum = 0
    for tree_height in tree_height_arr:
        if tree_height > mid:
            sum += tree_height - mid
            
    if sum >= TARGET: # 절단기 높이를 낮게해서 목표치보다 많은 나무를 잘랐다면
        s = mid + 1 # 절단기 높이를 높임
    elif sum < TARGET:  # 절단기 높이를 높게해서 목표치보다 적은 나무를 잘랐다면
        e = mid - 1 # 절단기 높이를 낮춤

    """
    부등호를 아래와 같이 변경한다면, 틀림
    
    왜냐하면 문제 조건에서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 것이 조건으로 제시되어 있으므로,
    sum이 TARGET 값과 동일하거나 혹은 크다는 상황은 절단기 높이가 낮아서 더 많은 나무를 자른 경우를 포함하므로
    절단기 높이를 더욱 높였을 때에도 sum이 TARGET 값과 동일할 수 있는 경우를 판별해야 함.
    
    그러나, 아래 elif문 같은 경우에는 sum이 TARGET 값과 동일한 경우 역시 절단기 높이를 더 낮춤. 
    따라서 절단기 높이를 더 높였을 때의 sum이 TARGET 값과 동일하거나 큰 경우는 판별할 수 없으므로, 
    아래와 같이 부등호를 변경한다면 정답이 될 수 없음.
    
    if sum > TARGET: 
        s = mid + 1 
    elif sum <= TARGET:  
        e = mid - 1 
        
    """

print(e)