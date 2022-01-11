# 도영이가 만든 맛있는 음식 (BOJ 2961)

n = int(input())
sour_bitter = []

for _ in range(n):
    sour_bitter.append(list(map(int, input().split())))
    
min_val = 1e9
def dfs(start, total_sour, total_bitter):
    global min_val
    
    if total_bitter != 0:
        min_val = min(min_val, abs(total_sour-total_bitter))
        
    for i in range(start, n):
        dfs(i+1, total_sour * sour_bitter[i][0], total_bitter + sour_bitter[i][1])
        
dfs(0, 1, 0)
print(min_val)