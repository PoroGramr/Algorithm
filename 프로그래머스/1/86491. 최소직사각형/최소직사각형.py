def solution(sizes):
    answer = 0
    wMax = 0
    hMax = 0
    nSizes = []
    for w,h in sizes:
        tmp = [w,h]
        tmp.sort()
        nSizes.append(tmp)
    
    for w,h in nSizes:
        wMax = max(wMax,w)
        hMax = max(hMax,h)
    
    answer = wMax * hMax
    
    
    return answer