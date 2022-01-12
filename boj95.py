# A와 B2 (BOJ 12919)

""" 아래 코드는 구글링 """
def dfs(s,t):
    if len(t) == len(s):
        if t == s:
            return 1
        return 0
    if t[-1] == 'A' and dfs(s,t[:-1]) == 1:
        return 1
    if t[0] == 'B' and dfs(s,t[::-1][:-1]) == 1:
        return 1
    return 0

s = input()
t = input()
print(dfs(s,t))

"""
아래 코드는 시간초과,

s = list(input())
t = list(input())

check = False
def dfs(s, t):
    global check
    
    if len(s) == len(t):
        if s == t:
            check = True
            print(1)
            exit(0)
        else:
            return
    
    s.append('A')
    dfs(s, t)
    s.pop()
    s.append('B')
    dfs(s[::-1], t)
    s.pop()
    
dfs(s, t)
if check == False:
    print(0)
    
"""