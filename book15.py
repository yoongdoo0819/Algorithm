# 문자열 뒤집기

n = input()

cnt = {'0':0, '1':0}
prev = n[0]

for idx in range(1, len(n)):
    curr = n[idx]
    if prev != curr:
        cnt[prev] += 1
        prev = curr

cnt[curr] += 1
min_val = min(cnt['0'], cnt['1'])
print(min_val)
    