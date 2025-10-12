def solution(s):
    
    parts = s[2:-2].split("},{")        
    sets = [list(map(int, p.split(','))) for p in parts]
    sets.sort(key=len)
    
    
    ans, seen = [], set()
    for s in sets:
        for num in s:
            if num not in seen:
                ans.append(num)
                seen.add(num)

    return ans