# 오픈채팅방

def solution(record):
    answer = []
    uidMap = dict()
    
    for str in record:
        inst = str.split(' ')
        if inst[0] == 'Enter' or inst[0] == 'Change':
            uidMap[inst[1]] =inst[2]
    
    for str in record:
        inst = str.split(' ')
        if inst[0] == 'Enter':
            msg = uidMap[inst[1]] + '님이 들어왔습니다.'
        elif inst[0] == 'Leave':
            msg = uidMap[inst[1]] + '님이 나갔습니다.'
        else:
            continue
        answer.append(msg)
        
    return answer