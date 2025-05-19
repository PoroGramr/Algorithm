'''
문제 이해

수도 코드
1.  
'''


def solution(nums):
    
    maxPoketmon = len(nums) / 2
    
    numset = set(nums)
    
    answer = 0
    if len(numset) < maxPoketmon:
        answer = len(numset)
    else:
        answer = maxPoketmon
    return answer