# 단어 뒤집기 2 (BOJ 17413)

input_str = input()

target_str = ''
check = False
for idx in range(0, len(input_str)):
    
    if (input_str[idx].isdigit() or 'a' <= input_str[idx] <= 'z') and check == False:
        target_str = input_str[idx] + target_str
    
    elif (input_str[idx].isdigit() or 'a' <= input_str[idx] <= 'z' or input_str[idx] == ' ') and check == True:
        target_str += input_str[idx]
        
    elif input_str[idx] == '<':
        print(target_str, end = '')
        target_str = input_str[idx]
        check = True
        
    elif input_str[idx] == ' ' and check == False:
        print(target_str, end = ' ')
        target_str = ''
    
    elif input_str[idx] == '>':
        print(target_str+input_str[idx], end = '')
        target_str = ''
        check = False  
    
if target_str != '':
    print(target_str)