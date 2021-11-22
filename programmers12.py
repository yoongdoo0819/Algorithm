# 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
    answer = []
    table = {}
    for num in course:
        table[num] = {}
        
    for order in orders:
        for num in course:
            order = list(order)
            course_menu_list = combinations(order, num)
            for course_menu_tuple in course_menu_list:
                #course_menu = 
                course_menu = "".join(sorted(course_menu_tuple))
                
                if not course_menu in table[num].keys():
                    table[num][course_menu] = 1
                else:
                    table[num][course_menu] += 1
                
    for num in course:
        if len(table[num]) == 0:
            continue
        max_val = max(table[num].values())
        if max_val < 2:
            continue
        for key, val in table[num].items():
            if val == max_val:
                answer.append(key)
                
    return sorted(answer)