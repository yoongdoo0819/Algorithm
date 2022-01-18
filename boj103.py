# 로프 (BOJ 2217)

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))
    
ropes.sort(reverse=True)
max_val = ropes[0]

for i, rope in enumerate(ropes):
    weight = rope * (i+1)
    if max_val < weight:
        max_val = weight
        
print(max_val)