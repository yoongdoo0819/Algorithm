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

"""
아래와 같은 코드가 틀리는 이유는
예를 들어 1, 12, 23, 3으로 카드 수가 존재한다고 할 때,
1, 23과 12, 3은 모두 123이지만, 다른 숫자로 여기게 되므로

from itertools import permutations

N = int(input())
K = int(input())
ans = []
cards = []

for _ in range(N):
    cards.append(int(input()))
    
for card in permutations(cards, K):
    if not card in ans:
        ans.append(card)

print(ans)
print(len(ans))
"""
