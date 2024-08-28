def sortKey(filename):
    head = ''
    number = ''
    
    isNumber = False
    
    for i,f in enumerate(filename):
        if f.isdigit():
            isNumber = True
            number += f
        else:
            if isNumber == True:
                break
            head += f
    head = head.lower()
    number = int(number)
    
    return(head, number)

def solution(files):
    answer = sorted(files, key=sortKey)
    return answer