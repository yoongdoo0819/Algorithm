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