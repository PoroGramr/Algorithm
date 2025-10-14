"""
기존 단품으로만 제공하던 메뉴를 코스 형태로 재 구성 하고자 함
이전에 각 손님들이 주문할 떄 가장 많이 함께 주문한 단품 메뉴들을 코스로 구성하고자 함
최소 2가지 이상의 단품 메뉴, 최소 2명 이상의 손님으로부터 주문된 조합
"""
from itertools import combinations

def solution(orders, course):
    count = {c: {} for c in course}
    
    for order in orders:
        for c in course:
            for comb in combinations(order,c):
                combList = list(comb)
                combList.sort()
                combStr = "".join(combList)
                if combStr in count[c]:
                    count[c][combStr] += 1
                else:
                    count[c][combStr] = 1
    
    answer = []

    
    
    for c in course:
        if not count[c]:
            continue
        countMax = max(count[c].values())
        for key, value in count[c].items():
            if value == countMax and countMax >= 2:
                answer.append(key)
    
    answer.sort()
    
    return answer