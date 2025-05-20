def dfs(numbers, target, i, currentSum):
    global answer
    if i == len(numbers):
        if currentSum == target:
            answer += 1
        return        
    
    dfs(numbers, target, i + 1, currentSum + numbers[i])
    
    dfs(numbers, target, i + 1, currentSum - numbers[i])
    
    
    

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0,0)
    return answer