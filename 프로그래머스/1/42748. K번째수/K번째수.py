def solution(array, commands):
    
    answer = []
    
    for i,j,k in commands:
        cutArray = array[i-1 : j]
        cutArray.sort()
        
        answer.append(cutArray[k-1])
    
    return answer