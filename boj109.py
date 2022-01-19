# 에너지 드링크 (BOJ 20115)

n = int(input())
energy_drink = list(map(int, input().split()))

energy_drink.sort(reverse=True)
sum = energy_drink[0]

for i in range(1, n):
    sum += energy_drink[i]/2
    
print(sum)