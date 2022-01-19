# 서강근육맨 (BOJ 20300)

n = int(input())
loss_of_muscle = list(map(int, input().split()))
loss_of_muscle.sort()
max_val = 0

if len(loss_of_muscle) % 2 == 1:
    dummy = -1
    last_len = 2
else:
    dummy = 0
    last_len = 1

j = len(loss_of_muscle) - last_len
for i in range(len(loss_of_muscle)//2 + dummy):
    temp = loss_of_muscle[i] + loss_of_muscle[j]
    j -= 1
    max_val = max(max_val, temp)

print(max_val)