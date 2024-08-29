def solution(land):
    answer = 0
    
    memo = []
    for i in range(len(land)):
        memo.append([0] * 4)
        
    memo[0] = land[0]
    # [[1, 2, 3, 5], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(1, len(land)):
        for j in range(4):
            # cols = [memo[i-1][k] for k in range(4) if k != j]
            cols = []
            for k in range(4):
                if k != j:
                    cols.append(memo[i-1][k])
            memo[i][j] = land[i][j] + max(cols)
            
    answer = max(memo[-1])        
        
    
    return answer