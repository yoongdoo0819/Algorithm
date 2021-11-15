# 연산자 끼워 넣기

n = int(input())
graph = (list(map(int, input().split())))
op = (list(map(int, input().split())))
opMap = {'+': op[0], '-': op[1], '*': op[2], '//': op[3]}

print(n, graph, op, opMap)

max_val = -1e9
min_val = 1e9

def dfs(graph, pos, result):
    global max_val, min_val
    
    if opMap['+'] == 0 and opMap['-'] == 0 and \
        opMap['*'] == 0 and opMap['//'] == 0:
            print("result ", result)
            return result

    if opMap['+'] > 0:
        opMap['+'] -= 1
        val = dfs(graph, pos+1, result + graph[pos])
        print("val1 : ", pos, val, result)
        opMap['+'] += 1
        max_val = max(val, max_val)
        min_val = min(val, min_val)
        
    if opMap['-'] > 0:
        opMap['-'] -= 1
        val = dfs(graph, pos+1, result - graph[pos])
        print("val2 : ", val)
        opMap['-'] += 1
        max_val = max(val, max_val)
        min_val = min(val, min_val)
        
    if opMap['*'] > 0:
        opMap['*'] -= 1
        val = dfs(graph, pos+1, result * graph[pos])
        print("val3 : ", pos, val, result)
        opMap['*'] += 1
        max_val = max(val, max_val)
        min_val = min(val, min_val)
        
    if opMap['//'] > 0:
        opMap['//'] -= 1
        
        # int(result/graph[pos])와 result//graph[pos] 차이 : int(-1/4)는 0, -1//4는 -1
        print("result / graph[pos] ", result, graph[pos], int(result/graph[pos]))
        print("result // graph[pos] ", result, graph[pos], result//graph[pos])
        val = dfs(graph, pos+1, int(result / graph[pos]))
        print("val4 : ", val)
        opMap['//'] += 1
        max_val = max(val, max_val)
        min_val = min(val, min_val)
    
    return max_val
        

dfs(graph, 1, graph[0])
print(max_val, min_val)