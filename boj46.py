# ZOAC 3 (BOJ 20436)


maps1 = {
    'q':'ㅂ', 'w':'ㅈ', 'e':'ㄷ', 'r':'ㄱ', 't':'ㅅ', 'y':'ㅛ', 'u':'ㅕ', 'i':'ㅑ', 'o':'ㅐ', 'p':'ㅔ',
    'a':'ㅁ', 's':'ㄴ', 'd':'ㅇ', 'f':'ㄹ', 'g':'ㅎ', 'h':'ㅗ', 'j':'ㅓ', 'k':'ㅏ', 'l':'ㅣ',
    'z':'ㅋ', 'x':'ㅌ', 'c':'ㅊ', 'v':'ㅍ', 'b':'ㅠ', 'n':'ㅜ', 'm':'ㅡ'
}

maps2 = {
    'ㅂ':(0, 0), 'ㅈ':(0, 1), 'ㄷ':(0, 2), 'ㄱ':(0, 3), 'ㅅ':(0, 4), 'ㅛ':(0, 5), 'ㅕ':(0, 6), 'ㅑ':(0, 7), 'ㅐ':(0, 8), 'ㅔ':(0, 9),
    'ㅁ':(1, 0), 'ㄴ':(1, 1), 'ㅇ':(1, 2), 'ㄹ':(1, 3), 'ㅎ':(1, 4), 'ㅗ':(1, 5), 'ㅓ':(1, 6), 'ㅏ':(1, 7), 'ㅣ':(1, 8),
    'ㅋ':(2, 0), 'ㅌ':(2, 1), 'ㅊ':(2, 2), 'ㅍ':(2, 3), 'ㅠ':(2, 4), 'ㅜ':(2, 5), 'ㅡ':(2, 6)
}

left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

left_hand, right_hand = input().split()
left_hand_x, left_hand_y = maps2[maps1[left_hand]]
right_hand_x, right_hand_y = maps2[maps1[right_hand]]

print_str = list(input())

total_dist = 0
for ch in print_str:
    target_x, target_y = maps2[maps1[ch]]
    if ch in left:
        total_dist += abs(left_hand_x - target_x) + abs(left_hand_y - target_y)
        left_hand_x, left_hand_y = target_x, target_y
    elif ch in right:
        total_dist += abs(right_hand_x - target_x) + abs(right_hand_y - target_y)
        right_hand_x, right_hand_y = target_x, target_y

total_dist += len(print_str)
print(total_dist)