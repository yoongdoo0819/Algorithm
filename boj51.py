# 기차가 어둠을 헤치고 은하수를 (BOJ 15787)

n, m = map(int, input().split())
maps = [ ['0'] * 21 for _ in range(n+1) ]

def solution():
    for _ in range(m):
        inst = list(map(int, input().split()))
        
        if len(inst) == 3:
            i, num, x = inst[0], inst[1], inst[2]
        elif len(inst) == 2:
            i, num = inst[0], inst[1]
        
        if i == 1:
            maps[num][x] = '1'
            
        elif i == 2:
            maps[num][x] = '0'
        
        elif i == 3:
            maps[num].insert(1, '0')
            maps[num].pop(-1)
        
        elif i == 4:
            maps[num].pop(1)
            maps[num].append('0')

solution()
train_dict = {}
cnt = 0
for idx in range(1, len(maps)):
    train = maps[idx]
    train = "".join(train)
    if not train in train_dict:
        train_dict[train] = 1
        cnt += 1
        
print(cnt)
    
