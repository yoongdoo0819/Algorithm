# 달력 (BOJ 20207)

n = int(input())

calendar = [0] * 367

for _ in range(n):
    start, end = map(int, input().split())
    calendar[start] += 1
    calendar[end+1] += -1
    

width, height = 0, 0
answer = 0
for i in range(1, 367):
    
    calendar[i] += calendar[i-1]
    if calendar[i] == 0:
        answer += width * height
        width, height = 0, 0
    else:
        width += 1
        height = max(calendar[i], height)
        
print(answer)