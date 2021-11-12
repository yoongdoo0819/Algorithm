# 왕실의 나이트

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

print(row, col)

steps = [ [-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2] ]
count = 0

for step in steps:
    x = row + step[0]
    y = col + step[1]
    
    if x <= 0 or x > 8 or y <= 0 or y > 8:
        continue
    else:
        count += 1

print(count)