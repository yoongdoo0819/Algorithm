# 게임 개발
import copy

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board, temp_board = [], []
for _ in range(n):
    inp = list(map(int, input().split())) 
    board.append(copy.deepcopy(inp))
    temp_board.append(copy.deepcopy(inp))
    
print(n, m)
print(x, y, d)

direction = [0, 1, 2, 3]
allDirectionCheck = 0

temp_board[x][y] = 1
cnt = 1

def getDirection(d):
    d -= 1
    if d == -1:
        d = 3
    return d

while True:
    
    d = getDirection(d)
    
    if d == 0: # 북쪽을 바라본다면
        if temp_board[x-1][y] == 0 and x-1 >= 0: 
            temp_board[x-1][y] = 1
            cnt += 1
            x = x - 1
            allDirectionCheck = 0
            continue
        
    elif d == 1: # 동쪽을 바라본다면
        if temp_board[x][y+1] == 0 and y+1 < m: 
            temp_board[x][y+1] = 1    
            cnt += 1
            y = y + 1
            allDirectionCheck = 0
            continue
        
    elif d == 2: # 남쪽을 바라본다면
        if temp_board[x+1][y] == 0 and x+1 < n: 
            temp_board[x+1][y] = 1
            cnt += 1
            x = x + 1
            allDirectionCheck = 0
            continue
        
    elif d == 3: # 서쪽을 바라본다면
        if temp_board[x][y-1] == 0 and y-1 >= 0: 
            temp_board[x][y-1] = 1
            cnt += 1
            y = y - 1
            allDirectionCheck = 0
            continue
    
    allDirectionCheck += 1
    print("curr x, y, d, direction, cnt", x, y, d, allDirectionCheck, cnt)
            
    if allDirectionCheck == 4:
        if d == 0: # 북쪽에서 한 칸 뒤로
            if board[x+1][y] == 0: #and x+1 < n:
                x = x + 1
                allDirectionCheck = 0
        elif d == 1: # 동쪽에서 한 칸 뒤로
            if board[x][y-1] == 0: #and y-1 >= 0:
                y = y - 1
                allDirectionCheck = 0
        elif d == 2: # 남쪽에서 한 칸 뒤로
            if board[x-1][y] == 0: # and y >= 0:
                x = x - 1
                allDirectionCheck = 0
        elif d == 3: # 서쪽에서 한 칸 뒤로
            if board[x][y+1] == 0: # and y+1 < m:
                y = y + 1
                allDirectionCheck = 0
        
        if allDirectionCheck == 4:
            break
        
print(cnt)
for col in temp_board:
    print(col)
    
print("======")
for col in board:
    print(col)