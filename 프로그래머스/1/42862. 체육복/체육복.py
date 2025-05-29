def solution(n, lost, reserve):
    # 현재 체육복이 있는 학생 수
    lost.sort()
    reserve.sort()
    lostSet = set(lost)
    reserveSet = set(reserve)
    
    both = lostSet & reserveSet
    lostSet -= both
    reserveSet -= both
    
    for stu in sorted(lostSet):
        if (stu - 1) in reserveSet:
            lostSet.remove(stu)
            reserveSet.remove(stu-1)
        elif (stu + 1) in reserveSet:
            lostSet.remove(stu)
            reserveSet.remove(stu+1)
    
    answer = n - len(lostSet)
    
    return answer