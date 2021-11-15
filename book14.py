# 곱하기 혹은 더하기

s = input()

total = int(s[0])
for i in range(1, len(s)):
    curr = int(s[i])
    if total <= 1 or curr <= 1:
        total += curr
    else:
        total *= curr
    
print(total)