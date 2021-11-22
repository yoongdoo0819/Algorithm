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