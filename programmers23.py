# 압축

def solution(msg):
    answer = []
    
    dict = {}
    for i in range(65, 91):
        dict[chr(i)] = i-64
        
    idx = 1
    sub_msg = msg[idx-1]
    while idx < len(msg):
        if (sub_msg + msg[idx]) in dict.keys():
            sub_msg += msg[idx]
            idx += 1
            continue
        else:
            #print(sub_msg, msg[idx], dict[sub_msg])
            answer.append(dict[sub_msg])
            dict[(sub_msg + msg[idx])] = max(dict.values()) + 1
            sub_msg = msg[idx]
            idx += 1
            
    #print(sub_msg, dict[sub_msg])
    answer.append(dict[sub_msg])
    return answer