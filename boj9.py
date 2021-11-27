# 요세푸스 문제

n, target_k = map(int, input().split())
arr = [ [] for _ in range(n)]

for i in range(0, n):
    arr[i].append(i+1)
    
result = []
k = 0
while arr.count(0) != n:
    
    for element in arr:
        if element != 0:
            k += 1
            
            if k == target_k:
                
                idx = arr.index(element)
                arr[idx] = 0
                k = 0
                result.append(element)
        
        elif element == 0:
            continue
      
print("<", end='')          
for element in result:
    if result.index(element) == 0:
        print(element[0], end='')
    
    else:
        print(",", element[0], end='')                      
print(">")  
                