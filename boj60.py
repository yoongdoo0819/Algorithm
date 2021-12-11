# N과 M (1) (BOJ 15649)

from itertools import permutations
n, m = map(int, input().split())

permutation_list = []
for i in range(1, n+1):
    permutation_list.append(i)
    
for val in permutations(permutation_list, m):
    for i in range(m):
        print(val[i], end =' ')
    print("")