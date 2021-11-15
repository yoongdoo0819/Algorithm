# 모험가 길드

n = int(input())
datas = list(map(int, input().split()))

datas.sort()
temp = []
cnt = 0
length = len(datas)

for data in datas:
    
    temp.append(data)
    if max(temp) == len(temp):
        cnt += 1
        temp = []
        
print(cnt)