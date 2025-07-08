from itertools import permutations

def solution(user_id, banned_id):
    idPermu = list(permutations(user_id, len(banned_id)))
    
    answers = set()
    
    for permu in idPermu:
        isMatch = True
        for i in range(len(permu)):
            cur = permu[i]
            ban = banned_id[i]
            
            if len(cur) != len(ban):
                isMatch = False
                break
            
            for j in range(len(ban)):
                if ban[j] == "*":
                    continue
                
                if ban[j] != cur[j]:
                    isMatch = False
                    break
            
            if not isMatch:
                break
            
        if isMatch:
            answers.add(tuple(sorted(permu)))
                
    
    answer = len(answers)
    return answer