'''
문제이해
각 종류별로 최대 1가지의 의상만 착용 가능
최소 1개의 의상은 입는다
서로 다른 옷의 조합의 수
'''

def solution(clothes):
    dic= {}
    for name, kind in clothes:
        dic[kind] = dic.get(kind, 0) + 1
    
    combinations = 1
    for count in dic.values():
        combinations *= (count + 1)
    
    answer = combinations - 1
    return answer