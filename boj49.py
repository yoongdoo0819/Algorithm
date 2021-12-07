# 원상 복구(small) (BOJ 22858)

n, k = map(int, input().split())

card = [0] * n
s = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

for _ in range(k):
    card = [0] * (n+1)
    for idx in range(1, n+1):
        card[d[idx]] = s[idx]
    s = card.copy()
        
for i in range(1, len(s)):
    print(s[i], end = ' ')