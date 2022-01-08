# 카드 놓기 (BOJ 5568)

from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    card_num = input()
    cards.append(card_num)
    
answer = set()
for card in permutations(cards, k):
    new_num_list = list(card)
    new_num = "".join(new_num_list)
    answer.add(new_num)
    
print(len(answer))