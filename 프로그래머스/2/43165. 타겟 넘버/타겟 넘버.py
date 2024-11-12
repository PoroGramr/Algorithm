def dfs(numbers, target, i, sm):
    global ans
    if i == len(numbers):
        if sm == target:
            ans += 1
        return
    
    dfs(numbers, target, i+1, sm + numbers[i])
    
    dfs(numbers, target, i+1, sm - numbers[i])
    
        


def solution(numbers, target):
    global ans
    ans = 0
    dfs(numbers,target, 0,0) # 인덱스, 지금까지의 합
    return ans