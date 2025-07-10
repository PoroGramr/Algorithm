from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for courseSize in course:
        allCombinations = []
        
        for order in orders:
            combs = combinations(sorted(order), courseSize)
            allCombinations.extend(combs)
        
        if not allCombinations:
            continue
            
        courseCounter = Counter(allCombinations)
        
        if courseCounter and max(courseCounter.values()) >= 2:
            maxOrderCount = max(courseCounter.values())
            
            for menu, count in courseCounter.items():
                if count == maxOrderCount:
                    answer.append("".join(menu))

    return sorted(answer)