# 여행경로 

"""
해결 방안 1과 2의 차이점 :

해결 방안 1에서는 src와 dst 경로 간 중복 티켓이 존재한다면,
list 자료구조를 사용하여 dsf 이전에 해당 list에서 dst를 삭제하고, dfs 직후 해당 list에 dst를 다시 추가하는 방식으로 중복 티켓을 허용함

해결 방안 2에서는 src와 dst를 map으로 표현하였으며, src와 dst 간 중복 티켓 수량만큼 +를 함
dfs 이전에 해당 map에서 수량을 -1하고, dfs 직후 수량을 +1 해줌으로써 중복 티켓을 허용함

그러나, 해결 방안 1은 히든 테케 1에서 대략 300ms 정도 소요되지만, 해결 방안 2는 2,000ms 정도 소요됨.
이런 속도 차이가 발생하는 이유는 ?
"""

""" 해결 방안 1"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

total_path = []
result = []
check = False

def dfs(src, tickets_list, n, visited):
    global total_path
    global result
    global check

    if len(result)-1 == n and check == False:
        total_path = result.copy()
        check = True
        return

    for dst in tickets_list[src]:
        if dst in visited[src]:
            result.append(dst)
            visited[src].remove(dst)
            dfs(dst, tickets_list, n, visited)
            visited[src].append(dst)
            result.pop()
        

def solution(tickets):

    test_map = {}
    
    """
    아래 tickets_list와 visited 초기화 시, tickets_list = {}로 초기화 이후 dfs를 구동하면 KeyError 발생 (visited 변수는 visited = {}로 초기화해도 KeyError 발생 안함).
    그러나 tikcets_list = defaultdict(list)로 초기화하면 Error 발생하지 않고 통과.
    
    그러나, dfs를 구동하면서 기존에 존재하지 않는 key로 tickets_list를 접근하지 않을텐데,,, 
    ***왜, 어느 부분에서 KeyError가 발생하는지 모름***
    """
    tickets_list = defaultdict(list)
    visited = defaultdict(list)
    
    print(not 'a' in tickets_list)
    print(not 'a' in test_map)
    
    print(tickets_list['a']) # [] 리턴
    #print(test_map['a']) KeyError 발생
    
    for src, dst in tickets:
        if not src in tickets_list:
            tickets_list[src] = []
        tickets_list[src].append(dst)

        if not src in visited:
            visited[src] = []
            visited[src].append(dst)
        elif src in visited:
            visited[src].append(dst)


    for key in tickets_list.keys():
        tickets_list[key].sort()

    result.append('ICN')
    dfs('ICN', tickets_list, len(tickets), visited)    

    return total_path

""" 해결 방안 2"""
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

total_path = []
result = []
check = False

def dfs(src, tickets_list, n, visited):
    global total_path
    global result
    global check
    
    if len(result)-1 == n and check == False:
        total_path = result.copy()
        check = True
        return
    
    for dst in tickets_list[src]:
        tikcet_num = visited[src][dst]
        for _ in range(0, tikcet_num):

            result.append(dst)
            visited[src][dst] -= 1
            dfs(dst, tickets_list, n, visited)
            visited[src][dst] += 1
            result.pop()
            
def solution(tickets):
    
    tickets_list = defaultdict(list)
    visited = {} # defaultdict(list)

    for src, dst in tickets:
        if not src in tickets_list:
            tickets_list[src] = []
        tickets_list[src].append(dst)
            
        if not src in visited:
            visited[src] = {}
            visited[src][dst] = 1
        elif src in visited and not dst in visited[src]:
            visited[src][dst] = 1
        else:
            visited[src][dst] += 1
        
    for key in tickets_list.keys():
        tickets_list[key].sort()
    
    result.append('ICN')
    dfs('ICN', tickets_list, len(tickets), visited)    
    print(tickets_list)
    print(visited)
    return total_path
"""