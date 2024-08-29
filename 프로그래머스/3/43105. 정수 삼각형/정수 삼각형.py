"""
- 삼각형을 뒤집는다.
- memo[i][j] = max(memo[i-1][j], memo[i-1][j+1]) + triangle[i][j]
- memo[-1][0]
"""
def solution(triangle):
    n = len(triangle) # 삼각형의 층수
    
    memo = []
    
    for i in range(n):
        memo.append([-1] * len(triangle[i]))
    # 	[[-1], [-1, -1], [-1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1, -1]]
    
    triangle.reverse()
    memo.reverse()
    
    memo[0] = triangle[0]
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            memo[i][j] = max(memo[i-1][j], memo[i-1][j+1]) + triangle[i][j]
            
    answer = memo[-1][0]
    return answer