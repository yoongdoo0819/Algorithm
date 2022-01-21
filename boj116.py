# 민겸 수 (BOJ 21314)

s = input()

"""
아래 코드에서 
각각의 16, 21, 30, 35 line은 46, 51, 60, 65 line과 동일

# 최댓값 구하기
max_s = s.split('K')
max_val = ''
for sub_s in max_s[:len(max_s)-1]:
    if sub_s == '':
        max_val += '5'
    else:
        max_val += '5' + len(sub_s) * '0'

if max_s[-1] == '':
    pass
else:
    max_val += '1' * (len(max_s[-1]))

# 최솟값 구하기
min_s = s.split('K')
min_val = ''
for sub_s in min_s[:len(min_s)-1]:
    if sub_s == '':
        min_val += '5'
    else:
        min_val += '1' + (len(sub_s)-1) * '0' + '5'

if min_s[-1] == '':
    pass
else:
    min_val += '1' + (len(min_s[-1])-1) * '0'

"""

# 최댓값 구하기
max_s = s.split('K')
max_val = ''
for sub_s in max_s[:len(max_s)-1]:
    if sub_s == '':
        max_val += '5'
    else:
        max_val += str(5 * (10 ** len(sub_s)))

if max_s[-1] == '':
    pass
else:
    max_val += '1' * (len(max_s[-1]))

# 최솟값 구하기
min_s = s.split('K')
min_val = ''
for sub_s in min_s[:len(min_s)-1]:
    if sub_s == '':
        min_val += '5'
    else:
        min_val += str(10 ** (len(sub_s)) + 5 )

if min_s[-1] == '':
    pass
else:
    min_val += str(10 ** (len(min_s[-1])-1))
    
print(max_val)
print(min_val)