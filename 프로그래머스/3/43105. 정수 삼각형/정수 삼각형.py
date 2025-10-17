"""
- 삼각형을 뒤집는다.
- memo[i][j] = max(memo[i-1][j], memo[i-1][j+1]) + triangle[i][j]
- memo[-1][0]
"""
def solution(triangle):
    
    n = len(triangle) # 삼각형의 층수
    
    memo = []
    
    for tri in triangle:
        memo.append(list(-1 for _ in range(len(tri))))
        
    triangle.reverse()
    memo.reverse()
    
    memo[0] = triangle[0]

    for y in range(1, n):
        for x in range(len(triangle[y])):
            memo[y][x] = max(memo[y-1][x], memo[y-1][x+1]) + triangle[y][x]
    
    answer = memo[-1][0]
    
    return answer