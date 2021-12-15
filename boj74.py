# 넴모넴모 (Easy) (BOJ 14712)


n, m = map(int, input().split())
graph = [ [0] * m for _ in range(n) ]

left_up_x = [-1, -1, 0]
left_up_y = [-1, 0, -1]
total_cnt = 0

def dfs(k):
    global total_cnt
    cnt = 0
    x, y = k//m, k%m # x, y 좌표를 구하는 방법. k번째 열이 m을 초과하면 행을 1 증가, k번째 열이 m을 초과하면 열은 0번째부터 시작
    
    if k == n*m:
        total_cnt += 1
        return
    
    for i in range(3):
        """
        왼, 위, 대각선왼쪽위 세 방향만 탐지하면 네모 완성 여부 판단 가능. 
        왜냐하면 (0, 0)부터 (0, 1), (0, 2)..., (0, m-1), (1, 0), (1, 1), ... (n-1, m-1) 순서대로 탐색하므로
        """
        nx = x + left_up_x[i]
        ny = y + left_up_y[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            break
        elif graph[nx][ny] == 1:
            cnt += 1
            
    if cnt < 3:
        graph[x][y] = 1
        dfs(k+1)
        graph[x][y] = 0

    dfs(k+1)
        
dfs(0)
print(total_cnt)