def solution(board, moves):
    answer = 0
    stack = [0, ]
    
    for move in moves:
        
        for col in board:
            
            if col[move-1] != 0:
                if stack[-1] == col[move-1]:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(col[move-1])
                    
                col[move-1] = 0
                break
                
    return answer