# 순위 검색

from bisect import bisect_left

languages = ['cpp', 'java', 'python']
works = ['backend', 'frontend']
careers = ['junior', 'senior']
foods = ['chicken', 'pizza']

def calc(table, lang, work, career, food, score):
    result = 0
    if lang == '-':
        for lang in languages:
            result += calc(table, lang, work, career, food, score)
    elif work == '-':
        for work in works:
            result += calc(table, lang, work, career, food, score)
    elif career == '-':
        for career in careers:
            result += calc(table, lang, work, career, food, score)
    elif food == '-':
        for food in foods:
            result += calc(table, lang, work, career, food, score)
    else:
        idx = bisect_left(table[lang][work][career][food], score)
        result += len(table[lang][work][career][food]) - idx

    return result
    
def solution(info, query):
    answer = []
    table = {}
    for language in languages:
        table[language] = {}
        for work in works:
            table[language][work] = {}
            for career in careers:
                table[language][work][career] = {}
                for food in foods:
                    table[language][work][career][food] = []
                
    for data in info:
        dataList = data.split()
        language = dataList[0]
        work = dataList[1]
        career = dataList[2]
        food = dataList[3]
        score = dataList[4]
        
        table[language][work][career][food].append(int(score))
    
    for language in languages:
        for work in works:
            for career in careers:
                for food in foods:
                    table[language][work][career][food].sort()
                    
                        
    for q in query:
        lang, _, work, _, career, _, food, score = q.split()
        result = calc(table, lang, work, career, food, int(score))
        answer.append(result)
        
    return answer