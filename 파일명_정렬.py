from operator import itemgetter

def solution(files):
    answer = []
    
    for file in files:
        
        idx = 0
        HEAD = ""
        NUMBER = ""
        TAIL = ""
        
        while idx < len(file):
            if not file[idx].isdigit():
                HEAD += file[idx]
                idx += 1
            else:
                break
                
        while idx < len(file):
            if file[idx].isdigit():
                NUMBER += file[idx]
                idx += 1
            else:
                break
            
        TAIL = file[idx:]
        answer.append([HEAD.lower(), int(NUMBER), TAIL, HEAD, NUMBER])
    
    answer.sort(key=itemgetter(0, 1))
    result = []
    for sortedFile in answer:
        str = sortedFile[3]
        str += sortedFile[4]
        str += sortedFile[2]
        result.append(str)
    
    return result