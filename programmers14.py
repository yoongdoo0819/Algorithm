# 튜플

def custom_list(string):
    result = []
    temp_list = []
    string = string[1:-1]
    string = string.replace(",", " ")
    conn_str = ""
    
    for idx in range(len(string)):
        str = string[idx]
        
        if str.isdigit():
            conn_str += str
        if str == '{':
            continue
        elif str == '}':
            temp_list = []
            split_strs = conn_str.split()
            for split_str in split_strs:
                temp_list.append(split_str)
            result.append(set(temp_list))
            temp_list = []
            conn_str = ""
        elif str == ' ':
            if string[idx+1].isdigit():
                conn_str += " "
            
    return result

def solution(s):
    answer = []
    s = custom_list(s)
    #print("list ", s)
    
    s.sort(key = lambda x : (len(x)) ) 
    #print("sorted", s)
    
    used_list = set()
    for data in s:
        if not data in used_list:
            diff = data - used_list
            answer.append(int(list(diff)[0]))
            used_list.update(data)
            
    return answer