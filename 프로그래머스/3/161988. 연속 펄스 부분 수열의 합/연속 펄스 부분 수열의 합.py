def solution(sequence):
    seLen = len(sequence)
    
    mPulse = []
    pPulse = []
    
    for i in range(seLen):
        if i % 2 == 0:
            mPulse.append(sequence[i] * -1)
            pPulse.append(sequence[i] * 1)
        else:
            mPulse.append(sequence[i] * 1)
            pPulse.append(sequence[i] * -1)
    
    maxSum1 = -9999999
    currentSum1 = 0
    
    maxSum2 = -9999999
    currentSum2 = 0
    
    for x in mPulse:
        currentSum1 = max(x, currentSum1 + x)
        maxSum1 = max(maxSum1, currentSum1)
        
    for y in pPulse:
        currentSum2 = max(y, currentSum2 + y)
        maxSum2 = max(maxSum2, currentSum2)
    answer = max(maxSum1, maxSum2)
    return answer