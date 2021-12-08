# ZOAC (BOJ 16719)

string = input() # list(input())
result = [''] * len(string)

def print_str(str_arr, start):
    if len(str_arr) == 0:
        return
    
    min_ch = min(str_arr)
    index = str_arr.index(min_ch)
    result[start+index] = min_ch
    print(''.join(result))
    
    print_str(str_arr[index+1:], start+index+1)
    print_str(str_arr[:index], start)

print_str(string, 0)
