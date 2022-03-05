# K번째수

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start, end, k = commands[i]
        new_arr = array[start-1:end]
        new_arr.sort()
        answer.append(new_arr[k-1])
    
    return answer