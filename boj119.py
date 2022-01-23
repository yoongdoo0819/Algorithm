# 숫자 카드 (BOJ 10815)

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
num_arr = list(map(int, input().split()))

for idx in range(m):
    s, e = 0, n-1 
    target = num_arr[idx]
    check = False
    
    while s <= e:
        mid = (s+e) // 2
        if cards[mid] == target:
            check = True
            break
        elif cards[mid] < target:
            s = mid + 1
        elif cards[mid] > target:
            e = mid - 1
        
    if check == True:
        print(1, end=' ')
    else:
        print(0, end=' ')