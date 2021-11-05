def divide_list(words, n):
    for i in range(0, len(words), n):
        yield words[i:i+n]

def solution(n, words):

    wordsDict = dict()
    for idx, val in enumerate(words):
        wordsDict[val] = 0

    words_list = list(divide_list(words, n))
    oneChar = words_list[0][0][0:1]

    for words_idx in range(0, len(words_list)):
        for person_idx in range(0, n):
            words = words_list[words_idx]
            if len(words) >= person_idx+1:
                if oneChar == words[person_idx][0:1]:
                    oneChar = words[person_idx][-1:]
                    wordsDict[words[person_idx]] += 1
                    if wordsDict[words[person_idx]] >= 2:
                        #print(person_idx+1, words_idx+1)
                        return [person_idx+1, words_idx+1]
                else:
                    return [person_idx+1, words_idx+1]
            else:
                break


    return [0, 0]