def solution(numbers):
    
    nums = list(map(str, numbers))
    max_len = max(len(s) for s in nums)
    nums.sort(key = lambda x : x * max_len, reverse=True) 
    answer = ''.join(nums)
    
    if nums[0] == '0':
        return '0'
    
    return answer