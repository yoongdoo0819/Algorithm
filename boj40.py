# 빙고 (BOJ 2578)

maps = []
del_num_list = []

for i in range(5):
    maps.append(list(map(int, input().split())))
    
for i in range(5):
    del_num_list.append(list(map(int, input().split())))
    


def bingo():
    bingo_cnt = 0
    
    # 가로 체크
    for i in range(5):
        bingo_check = True
        for j in range(5):
            if maps[i][j] != -1:
                bingo_check = False
                break
        if bingo_check == True:
            bingo_cnt += 1
    
    # 세로 체크
    for i in range(5):
        bingo_check = True
        for j in range(5):
            if maps[j][i] != -1:
                bingo_check = False
                break
        if bingo_check == True:
            bingo_cnt += 1
    
    # 0,0에서 4,4 대각선 체크
    bingo_check = True
    for i in range(5):
        if maps[i][i] != -1:
            bingo_check = False
            break
    if bingo_check == True:
        bingo_cnt += 1
        
    # 0,4에서 4,0 대각선 체크
    bingo_check = True
    for i in range(5):
        if maps[i][4-i] != -1:
            bingo_check = False
            break
    if bingo_check == True:
        bingo_cnt += 1
    
    if bingo_cnt >= 3:
        return True
    else:
        return False

def del_func(del_num):
    for i in range(5):
        for j in range(5): 
            if maps[i][j] == del_num:
                maps[i][j] = -1
                return True
    return False

def solution():
    cnt = 0
    for i in range(5):
        for j in range(5):
            del_func(del_num_list[i][j])
            cnt += 1
            if cnt >= 12:
                if bingo() == True:
                    return cnt
                
    return cnt

print(solution())
