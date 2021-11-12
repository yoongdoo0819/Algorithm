# 카드 정렬하기
import heapq

n = int(input())
cards = []

for i in range(n):
    cards.append(int(input()))
    
count = 0
heapq.heapify(cards)

while len(cards) > 2:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    newCard = card1+card2
    heapq.heappush(cards, newCard)
    count += newCard
    
card1 = heapq.heappop(cards)
card2 = heapq.heappop(cards)
newCard = card1 + card2
count += newCard

print(count)