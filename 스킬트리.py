def solution(skill, skill_trees):
    
    answer = 0
    skill = list(skill)    
    
    for i, skill_tree in enumerate(skill_trees):
        skillIdx = 0

        for idx in range(0, len(skill_tree)):
            if skill_tree[idx] in skill and skill_tree[idx] == skill[skillIdx]:
                skillIdx += 1
            elif skill_tree[idx] in skill and skill_tree[idx] != skill[skillIdx]:
                break

        else:
            answer += 1
    
    return answer