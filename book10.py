# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())

cityData = [ [] for _ in range(n+1) ]
print(cityData)

for i in range(0, m):
    src, dest = map(int, input().split())
    cityData[src].append(dest)

distance = [-1] * (n + 1)
distance[x] = 0
print(cityData)

q = deque([x])
print(q)

while q:
    now = q.popleft()
    
    for dest in cityData[now]:
        if distance[dest] == -1:
            distance[dest] = distance[now] + 1
            q.append(dest)
            
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
    
