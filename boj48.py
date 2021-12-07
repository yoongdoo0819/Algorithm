# 오목 (BOJ 2615)

n = 19
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))
    
def left_to_right_diagonal(x, y, color):
    
    cnt = 1
    
    temp_x, temp_y = x-1, y-1
    while 0 <= temp_x and 0 <= temp_y and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x -= 1
        temp_y -= 1
    
    temp_x, temp_y = x+1, y+1
    while temp_x < 19 and temp_y < 19 and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x += 1
        temp_y += 1
    
    if cnt == 5:
        return True
    else:
        return False
    

def left_to_right(x, y, color):

    cnt = 1
    
    temp_x, temp_y = x, y-1
    while 0 <= temp_y and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_y -= 1
    
    temp_x, temp_y = x, y+1
    while temp_y < 19 and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_y += 1
    
    if cnt == 5:
        return True
    else:
        return False

def right_to_left_diagonal(x, y, color):
    
    cnt = 1
    
    temp_x, temp_y = x-1, y+1
    while 0 <= temp_x and temp_y < 19 and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x -= 1
        temp_y += 1
    
    temp_x, temp_y = x+1, y-1
    while temp_x < 19 and 0 <= temp_y and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x += 1
        temp_y -= 1
    
    if cnt == 5:
        return True, temp_x-1, temp_y+1
    else:
        return False, 0, 0
    
def up_to_down(x, y, color):
    cnt = 1
    
    temp_x, temp_y = x-1, y
    while 0 <= temp_x and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x -= 1
        
    temp_x, temp_y = x+1, y
    while temp_x < 19 and maps[temp_x][temp_y] == color :
        cnt += 1
        temp_x += 1
    
    if cnt == 5:
        return True
    else:
        return False
    
def find_five(x, y, color):
    
    if left_to_right_diagonal(x, y, color) == True:
        return True
    
    if left_to_right(x, y, color) == True:
        return True
    
    check, ans_x, ans_y = right_to_left_diagonal(x, y, color)
    if check == True:
        print(color)
        print(ans_x+1, ans_y+1)
        exit()
    
    if up_to_down(x, y, color) == True:
        return True
    return False

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            if find_five(i, j, 1) == True:
                print(1)
                print(i+1, j+1)
                exit()
        elif maps[i][j] == 2:
            if find_five(i, j, 2) == True:
                print(2)
                print(i+1, j+1)
                exit()
                
print(0)