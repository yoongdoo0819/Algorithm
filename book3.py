# 숫자 카드 게임

n, m = map(int, input().split())

result = []
for i in range(n):
    cards = list(map(int, input().split()))
    result.append(min(cards))
    
max_val = max(result)
print(max_val)