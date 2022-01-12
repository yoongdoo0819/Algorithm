# 거스름돈 (BOJ 14916)

n = int(input())
cnt = 0

while n >= 2:
    
    if n >= 5 and n % 5 == 0:
        cnt += int(n/5)
        n = 0
        break
    
    if n >= 2:
        cnt += 1
        n -= 2

if n > 0:
    print(-1)
else:
    print(cnt)   
