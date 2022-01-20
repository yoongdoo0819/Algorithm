# 잃어버린 괄호 (BOJ 1541)

s = input()
expr_s = ''
copy_s = ''
temp_s = ''

"""
아래 코드는 구글링

arr = s.split('-') 
print(arr)
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j)
print(s)

"""

for i in range(len(s)):
    
    if s[i] == '+' or s[i] == '-':
        temp_s = str(int(temp_s))
        expr_s += temp_s + s[i]
        temp_s = ''
    else: 
        temp_s += s[i]
expr_s += str(int(temp_s))

minus_check = False
for i in range(len(expr_s)):
    
    if expr_s[i] == '-' and minus_check == False:
        copy_s += expr_s[i] + '('
        minus_check = True
    elif expr_s[i] == '-' and minus_check == True:
        copy_s += ')' + expr_s[i] + '('
    else:
        copy_s += expr_s[i]
if minus_check == True:
    copy_s += ')'
    
#print(s)
#print(expr_s)
#print(copy_s)
print(eval(copy_s))
