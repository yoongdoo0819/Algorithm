# ATM (BOJ 11399)

n = int(input())
people = list(map(int, input().split()))

people.sort()
ans = 0

for idx in range(n):
    temp = 0
    for i in range(0, idx+1):
        temp += people[i] #* (i + 1)
    ans += temp
    
print(ans)