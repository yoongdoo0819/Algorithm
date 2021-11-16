# 프렌즈4블록

def solution(m, n, board):
    answer = 0
    
    tempBoard = []
    for col in board:
        tempBoard.append(list(col))
    
    removeList = []
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if tempBoard[i][j] != '0' and tempBoard[i][j] == tempBoard[i][j+1] \
                and tempBoard[i][j] == tempBoard[i+1][j] == tempBoard[i+1][j+1]:
                    removeList.append((i, j))
                    removeList.append((i, j+1))
                    removeList.append((i+1, j))
                    removeList.append((i+1, j+1))

        if len(removeList) == 0:
            return answer
        
        for removeData in set(removeList):
            x, y = removeData
            tempBoard[x][y] = '0'
            answer += 1
        removeList = []
        
        for i in range(1, m-1):
            for j in range(n):
                #print(tempBoard[-i][j])
                if tempBoard[-i][j] == '0':
                    x, y = -i, j
                    while abs(x) <= m:
                        if tempBoard[x][y] != '0':
                            tempBoard[-i][j] = tempBoard[x][y]
                            tempBoard[x][y] = '0'
                            break
                        x -= 1
                
    
    return answer