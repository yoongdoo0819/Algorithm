# 큰 수 구성하기 (BOJ 18511)

n, k = map(int, input().split())
elements = list(input().split())
answer = int(elements[0])

def find_biggest(new_str):
    global answer
    
    """
    n = 1938이고 k 배열은 {8,9,7} 이라면 답은 999.
    
    따라서 아래와 같이 코드를 작성하면, 
    new_str이 1938과 동일하게 네 자리 수를 만족할 때만 조건문을 실행하게 됨.
    따라서 정답인 999와 같이 세 자리 수를 정답으로 출력할 수 없음.
    
    if len(new_str) == len(str(n)):
        
        new_int = int(new_str)
        if new_int > answer and new_int <= n:
            answer = new_int
        return
    
    그러므로, 
    아래처럼 만들어지는 모든 new_str 값과 n을 비교하면서 답을 갱신하고,
    new_str이 n과 동일한 자리수와 같아진다면 해당 dfs 함수를 종료하도록 함
    """
    if new_str != "":
        new_int = int(new_str)
        if new_int > answer and new_int <= n:
            answer = new_int
            
    if len(new_str) == len(str(n)):
        return
    
    if len(elements) >= 1:
        find_biggest(new_str+elements[0])

    if len(elements) >= 2:
        find_biggest(new_str+elements[1])
    
    if len(elements) >= 3:
        find_biggest(new_str+elements[2])

find_biggest("")
print(answer)

"""
아래 코드와 동일

N, K = map(int, input().split())
num_arr = list(input().split())

max_val = 0
def dfs(sum):
    global max_val
    
    if len(sum) == len(str(N))+1:    
        return
    
    if sum != '' and int(sum) <= N:    
        max_val = max(max_val, int(sum))
    
    for num in num_arr:
        dfs(sum + num)
        
dfs('')
print(max_val)

"""