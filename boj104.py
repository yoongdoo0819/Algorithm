# 폴리오미노 (BOJ 1343)

board = input()

splited_board = board.split('.')
ans_board = ''
ans = 0

for s in splited_board:
    if s == '':
        continue
    else:
        if len(s) % 2 != 0:
            ans = -1
            break
        
        temp_board = ''
        while len(s) % 2 == 0:
            if s == '':
                break
            
            if len(s) >= 4:
                temp_board += 'AAAA'
                s = s[4:]
            elif len(s) >= 2:
                temp_board += 'BB'
                s = s[2:]
                
        ans_board += temp_board        
        
if ans == -1:
    print(-1)
    exit(0)
else:
    idx = 0
    for s in board:
        if s == '.':
            print(s, end='')
        else:
            print(ans_board[idx], end='')
            idx += 1