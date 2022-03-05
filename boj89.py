# 퇴사 (BOJ 14501)


# 아래는 직접 짠 코드
N = int(input())

datas = []
for _ in range(N):
    x, y = map(int, input().split())
    datas.append((x, y))
    
ans = 0
def dfs(start, sum):
    global ans
    
    ans = max(ans, sum)
    
    for i in range(start, N):
            
        day, pay = datas[i]
        if i + day <= N:
            #print(">>", i+1, i+day+1, sum+pay)
            dfs(i+day, sum+pay)
            
dfs(0, 0)
print(ans)

"""
위 코드가 아래 코드보다 깔끔

n = int(input())

work_days = []

for _ in range(n):
    required_days, cost = map(int, input().split())
    work_days.append([required_days, cost])
    
result = [0]
max_val = 0
def get_highest_profit(start, accumulated_profit):
    global max_val
    
    for i in range(start, n):
        
        if i + work_days[i][0] <= n:
            temp = get_highest_profit(i + work_days[i][0], accumulated_profit + work_days[i][1])
            result.append(temp)
            max_val = max(max_val, temp)
    
    return accumulated_profit

get_highest_profit(0, 0)
#print(max(result))
print(max_val)

"""