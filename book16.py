# 만들 수 없는 금액

from itertools import combinations

n = int(input())
datas = list(map(int, input().split()))
datas.sort()
target = 1

while True:
    
    check = False
    
    if target in datas:
        target += 1
        continue
    
    for idx in range(1, len(datas)):
        
        for data in combinations(datas, idx):
            sum_val = sum(data)
            if sum_val == target:
                target += 1
                check = True
                break
            
        if check == True:
            break
    
    if check == False:
        print(target)
        break


"""
# book answer
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
    
print(target)
"""
