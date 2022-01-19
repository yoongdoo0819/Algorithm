# 2+1 세일 (BOJ 11508)

n = int(input())
item = []

for _ in range(n):
    item.append(int(input()))
    
item.sort(reverse=True)
ans = 0

for i in range(0, n, 3):
    temp_item = []
    temp_item.append(item[i])
    if i+1 < len(item):
        temp_item.append(item[i+1])
    if i+2 < len(item):
        temp_item.append(item[i+2])
    
    price = sum(temp_item)
    if len(temp_item) == 3:
        price -= min(temp_item)
    ans += price
    
print(ans)