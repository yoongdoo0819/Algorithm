# 후보키

from itertools import combinations

def get_all_min_subset(unique_set_list):
    
    min_set_list = []
    unique_set_list = sorted(unique_set_list, key = lambda x : len(x))
    
    for unique_set in unique_set_list:
        
        unique_set = set(unique_set)
        check = True
        
        for min_set in min_set_list:
            diff = min_set - unique_set
            if len(diff) == 0:
                check = False
                break
        if check == True:
            min_set_list.append(unique_set)
            
    return min_set_list

def get_all_unique_subset(relation, all_subset_idx_list):
    
    unique_set_list = []
    for subset_idx in all_subset_idx_list:
        
        candidate_key_list = []
        check = True
        for row_idx in range(0, len(relation)):
            
            candidate_key = ""
            for col_idx in subset_idx:
                candidate_key += relation[row_idx][col_idx]  
            
            if candidate_key in candidate_key_list:
                check = False
                break
            else:
                candidate_key_list.append(candidate_key)
                
        if check == True:
            unique_set_list.append(subset_idx)
    
    return unique_set_list

def get_all_subset_idx(idx_list):
    all_subset_idx_list = []
    for i in range(0, len(idx_list)+1):
        for subset_idx in combinations(idx_list, i):
            all_subset_idx_list.append(subset_idx)
    return all_subset_idx_list

def solution(relation):
    answer = 0
    idx_list = []
    for idx, col in enumerate(relation[0]):
        idx_list.append(idx)
        
    all_subset_idx_list = get_all_subset_idx(idx_list)
    unique_set_list = get_all_unique_subset(relation, all_subset_idx_list)
    min_set = get_all_min_subset(unique_set_list)
    
    return len(min_set)