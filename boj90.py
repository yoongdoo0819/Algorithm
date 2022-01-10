# 전공책 (BOJ 16508)

t = input()
n = int(input())

target_char_cnt = [ 0 for _ in range(26) ]
major_book_char_cnt = [ 0 for _ in range(26) ]

min_val = 1e9
books = []

for i in t:
    target_char_cnt[ord(i) - ord('A')] += 1

for _ in range(n):
    price, title = input().split()
    price = int(price)
    books.append((price, title))
    
def check():
    for i in range(26):
        if target_char_cnt[i] > major_book_char_cnt[i]:
            return False
    return True
     
def dfs(idx, total_price):
    global min_val
    
    if idx == n:
        if check() == True:
            min_val = min(min_val, total_price)
        return
    
    for j in books[idx][1]:
        major_book_char_cnt[ord(j) - ord('A')] += 1
    dfs(idx+1, total_price + books[idx][0])
    
    for j in books[idx][1]:
        major_book_char_cnt[ord(j) - ord('A')] -= 1
    dfs(idx+1, total_price)
    
dfs(0, 0)
if min_val == 1e9:
    print(-1)
else:
    print(min_val)