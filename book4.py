# 1이 될 때까지

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    
    print(n)
    count += 1
    
print(count)