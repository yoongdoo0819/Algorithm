# 폴더 정리 (small) (BOJ 22860)

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

idx = 0
file_maps = {'main':idx}
idx += 1
file_system = [ [] for _ in range(n+1) ]

for _ in range(n+m):
    folder, b, c = input().split()
    if c == '1':
        
        if not folder in file_maps:
            file_maps[folder] = idx
            idx += 1

        if not b in file_maps:
            file_maps[b] = idx
            idx += 1

    if folder in file_maps:
        file_system[file_maps[folder]].append((b, c))
        
total_file, file_cnt = 0, 0
dup_idx = 0

def dfs(start, visited, duplication):
    global total_file
    global file_cnt
    global dup_idx 
    visited[start] = True
    
    for next in file_system[start]:
        name, folder_or_file = next
        if folder_or_file == '1' and not visited[file_maps[name]]:
            dfs(file_maps[name], visited, duplication)
        elif folder_or_file == '0': 
            total_file += 1
            if not name in duplication:
                file_cnt += 1
                duplication[name] = 0    
    
loop_cnt = int(input())
for _ in range(loop_cnt):
    inst = input().split('/')
    folder = inst[-1]
    
    visited = [False] * (n+1)
    duplication = {}
    total_file, file_cnt = 0, 0
    dfs(file_maps[folder], visited, duplication)
    print(file_cnt, total_file)
