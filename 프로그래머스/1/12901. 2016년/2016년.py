def solution(a, b):
    Month = [31,29,31,30,31,30,31,31,30,31,30,31]
    Days = ["THU","FRI","SAT","SUN","MON","TUE","WED",]
    
    Alldays = 0
    
    for i in range(0,a - 1):
        Alldays += Month[i]
        
    Alldays += b
    
    return Days[Alldays % 7]
    
    
    
        