# 파일 정리 (BOJ 20291)

n = int(input())

maps = {}

for _ in range(n):
    file = input().split('.')
    if not file[1] in maps.keys():
        maps[file[1]] = 1
    else:
        maps[file[1]] += 1
    
file_list = []
for key, val in maps.items():
    file_list.append((key, val))
    
file_list = sorted(file_list, key = lambda x: x[0])
for extend, num in file_list:
    print(extend, num)
    
