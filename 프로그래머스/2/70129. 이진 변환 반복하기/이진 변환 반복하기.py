def solution(s):
    zeroC = 0
    loopC = 0
    while len(s) != 1:
        zeroC += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        loopC += 1
        
    return [loopC, zeroC]