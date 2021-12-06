# 스위치 켜고 끄기 (BOJ 1244)

m = int(input())
switch = list(map(int, input().split()))
switch.insert(0, -1)

std_num = int(input())
for _ in range(std_num):
    sex, switch_num = map(int, input().split())
    
    if sex == 1:
        plus = switch_num
        while 0 < switch_num < len(switch):
            if switch[switch_num] == 1:
                switch[switch_num] = 0
            else:
                switch[switch_num] = 1
            switch_num = switch_num + plus
            
    elif sex == 2:
        left, right = switch_num-1, switch_num+1
        
        while left > 0 and right < len(switch):
            
            if switch[left] == switch[right]:
                left -= 1
                right += 1
            else:
                break
        
        for i in range(left+1, right):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
            
cnt = 21
for i in range(1, len(switch)):
    if i % cnt == 0:
        print("")
        cnt += 20
    print(switch[i], end = ' ')