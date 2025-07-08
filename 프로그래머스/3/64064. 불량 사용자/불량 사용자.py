from itertools import permutations

def solution(user_id, banned_id):
    banned_count = len(banned_id)
    
    user_permutation = list(permutations(user_id, banned_count))
    
    banned_set = set()
    
    for perm in user_permutation:
        is_match = True
        
        for i in range(banned_count):
            user = perm[i]
            banned = banned_id[i]
            
            if len(user) != len(banned):
                is_match = False
                break
                
            for j in range(len(user)):
                if banned[j] == "*":
                    continue
                
                if user[j] != banned[j]:
                    is_match = False
                    break
            
            if not is_match:
                break
        
        if is_match:
            banned_set.add(tuple(sorted(perm)))
            
    answer = len(banned_set)
    return answer