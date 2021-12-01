# 숫자고르기

from copy import deepcopy

n = int(input())
maps = [ [] for _ in range(n+1) ]

for dst in range(1, n+1):
    src = int(input())
    maps[src].append(dst)
    

val_set = set()
check = [False] * (n+1)

def dfs(start, visited):
    global val_set
    visited.add(start)
    #check[start] = True
    
    for next in maps[start]:
        if not next in visited:
            dfs(next, deepcopy(visited))
        else:
            val_set = val_set | visited

for i in range(1, n+1):
    #if check[i] == False:
    visited = set()
    dfs(i, visited)
    
print(len(val_set))
"""
집합(set)은 순서가 없으므로 정렬되서 저장 되지 않음,
그러나 print로 집합 전체를 출력할 때는 자동으로 정렬해서 출력해줌. 
따라서 집합에 있는 값 전체를 출력하는 것이 아닌 
정렬된 상태로 하나씩 출력하고자 한다면 list로 변환 후,
정렬을 적용한 이후에 출력해줘야 함.
"""
for val in sorted(list(val_set)): 
    print(val)
    
""" 
# 조합으로 완전탐색 시도, 시간초과 발생
from itertools import combinations

n = int(input())
maps = []

for i in range(n):
    maps.append((i+1, int(input())))

max_set = set()
for i in range(n):
    
    for list in combinations(maps, i):
        if len(list) == 0:
            continue
        
        index_set = set()
        val_set = set()
        for list_val in list:
            index, val = list_val
            index_set.add(index)
            val_set.add(val)
        
        if index_set == val_set:
            if len(index_set) > len(max_set) :
                max_set = index_set 
           
print(len(max_set))
for val in max_set:
    print(val)
"""