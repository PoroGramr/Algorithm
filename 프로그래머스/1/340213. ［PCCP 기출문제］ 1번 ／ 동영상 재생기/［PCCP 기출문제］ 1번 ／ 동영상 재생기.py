"""
10초전, 10초후, 오프닝 건너뛰기
"""
def opSkip(cur,st,en):
    # 오프닝 시간에 들어갔따면
    if cur >= st and cur <= en:
        return en
    
    # 아니라면 그냥 그대로 리턴
    else:
        return cur
    
def solution(video_len, pos, op_start, op_end, commands):
    
    # 비디오의 길이 분,초를 변수에 저장
    endMin, endSec = video_len.split(":")
    endMin = int(endMin)
    endSec = int(endSec)
    end = endMin * 60 + endSec
    
    # 현재 분,초를 변수에 저장
    curMin, curSec = pos.split(":")
    curMin = int(curMin)
    curSec = int(curSec)
    cur = curMin * 60 + curSec

    # 오프닝 시작 시간 분,초를 변수에 저장
    stOpMin,stOpSec = op_start.split(":")
    stOpMin = int(stOpMin)
    stOpSec = int(stOpSec)
    st = stOpMin * 60 +stOpSec
    
    # 오프닝 종료 시간 분,초를 변수에 저장
    enOpMin,enOpSec = op_end.split(":")
    enOpMin = int(enOpMin)
    enOpSec = int(enOpSec)
    en = enOpMin * 60 +enOpSec
    
    for com in commands:
        # 오프닝 시간인지 확인
        cur = opSkip(cur,st,en)
        if com == "next":
            
            cur += 10
            
            if cur > end:
                cur = end
                
            
            
        elif com == "prev":
            cur -= 10
            
            if cur < 0:
                cur = 0
        # 오프닝 시간인지 확인
        cur = opSkip(cur,st,en)
                
            
    
    finMin = str(cur // 60)
    finSec = str(cur % 60)
    if len(finMin) == 1:
        finMin = "0" + finMin
    
    if len(finSec) == 1:
        finSec = "0" + finSec
    
    answer = finMin +  ":" + finSec
    return answer