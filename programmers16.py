# 전화번호 목록

def solution(phone_book):
    
    phone_book.sort()
    prev_phone = phone_book[0]
    for idx in range(1, len(phone_book)):
        curr_phone = phone_book[idx]
        if curr_phone.startswith(prev_phone, 0) == True:
            return False
        else:
            prev_phone = curr_phone
    
    return True

"""
풀이방법 2 (코드는 거의 유사).

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    hashMap = {}
    
    for i in range(0, len(phone_book)-1):
        phone = phone_book[i]
        if not phone in hashMap:
            hashMap[phone] = 1
        else:
            hashMap[phone] += 1
            
        next_phone = phone_book[i+1]
        if next_phone[:len(phone)] in hashMap:
           return False
        
        
    return answer

"""