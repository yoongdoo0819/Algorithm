# DNA (BOJ 1969)

n, m = map(int, input().split())
dna_list = []

for _ in range(n):
    dna_list.append(list(input()))
    
shortest_hamming_dist_dna = ''
hamming_dist_sum = 0

def get_hamming_distance(col):
    get_one_dna = {}
    for row in range(n):
        if not dna_list[row][col] in get_one_dna:
            get_one_dna[dna_list[row][col]] = 1
        else:
            get_one_dna[dna_list[row][col]] += 1
            
    max_val_list = []
    max_val = max(get_one_dna.values())
    for k, v in get_one_dna.items():
        if max_val == v:
            max_val_list.append(k)
            
    if len(max_val_list) >= 2:
        max_val_list.sort()
    
    return max_val_list[0], n-max_val
            
for col in range(m):
    max_val, hamming_dist_val = get_hamming_distance(col)
    shortest_hamming_dist_dna += max_val
    hamming_dist_sum += hamming_dist_val
    
print(shortest_hamming_dist_dna)
print(hamming_dist_sum)