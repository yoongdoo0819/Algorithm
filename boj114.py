# 동전 0 (BOJ 11047)

n, target_coin = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
    
coins.sort(reverse=True)
ans = 0
for idx, coin in enumerate(coins):
    
    if target_coin % coin == 0:
        ans += target_coin // coin 
        break
    elif coin > target_coin:
        continue
    elif coin < target_coin:
        num_of_coins = target_coin // coin
        ans += num_of_coins
        target_coin -= num_of_coins * coin
        if target_coin == 0:
            break
        
print(ans)