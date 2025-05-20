def solution(prices):
    answer = []
    # 최대값으로 기본값 설정
    for i in range(len(prices) - 1,-1,-1):
        answer.append(i)
    
    for i in range(len(answer)):
        for k in range(i, len(answer)):
            if prices[i] > prices[k]:
                answer[i] = k - i
                break
    
    return answer