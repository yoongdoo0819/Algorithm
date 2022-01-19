# 알바생 강호 (BOJ 1758)

n = int(input())
tips = []

for _ in range(n):
    tips.append(int(input()))
    
tips.sort(reverse=True)
ans = 0

for i in range(1, n+1):
    tip = tips[i-1] + 1 - i
    if tip <= -1:
        break
    else:
        ans += tip
        
print(ans)