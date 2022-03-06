# 단어 변환

from collections import deque

def bfs(begin, target, words, visited):
    q = deque()
    q.append(begin)
    
    while q:
        word = q.popleft()
        
        for target_word in words:
            
            if visited[target_word] == 0:
                check = 0
                for i in range(0, len(target_word)):
                    if word[i] == target_word[i]:
                        check += 1

                if check == len(word) - 1:
                    visited[target_word] = visited[word] + 1
                    q.append(target_word)

def solution(begin, target, words):
    
    visited = {}
    visited[begin] = 0
    visited[target] = 0
    
    for word in words:
        visited[word] = 0
        
    bfs(begin, target, words, visited)
    return visited[target]


"""
아래 코드는 위 코드처럼 visited 변수를 안 쓰는 대신, 각 단어마다 cnt를 붙여서 해결

from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append((begin, 0))
    
    while q:
        curr_word, cnt = q.popleft()
        
        if curr_word == target:
            return cnt
        
        for word in words:
            if curr_word == word:
                continue
            
            temp_cnt = 0
            for idx in range(len(curr_word)):
                if curr_word[idx] != word[idx]:
                    temp_cnt += 1
            
            if temp_cnt == 1 :
                q.append((word, cnt+1))
    return 0

def solution(begin, target, words):
    
    answer = bfs(begin, target, words)
    return answer

"""