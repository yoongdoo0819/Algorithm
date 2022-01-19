# 주유소 (BOJ 13305)

n = int(input())
dist = list(map(int, input().split()))
oil_price_for_curr_city = list(map(int, input().split()))
    
ans = 0
for i in range(n-1):
    required_oil_price = oil_price_for_curr_city[i] * dist[i]
    ans += required_oil_price
    
    if oil_price_for_curr_city[i] < oil_price_for_curr_city[i+1]:
        oil_price_for_curr_city[i+1] = oil_price_for_curr_city[i]
        
print(ans)