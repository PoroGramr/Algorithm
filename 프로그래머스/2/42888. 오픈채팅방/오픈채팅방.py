"""
닉네임을 변경하는 방식은 2가지
1. 나간 후 새로운 닉네임으로 다시 들어온다.
2. 채팅방에서 닉네임을 변경한다.

1안 단순 구현
1. 1234 입장 -> 결과 삽입
2. 4567 입장 -> 결과 삽입
3. 1234 퇴장 -> 결과 삽입
4. 1234 이름 수정 후 입장-> 결과 탐색 후 <N> 수정 및 삽입
5. 4567 이름 수정 -> 결과 탐색 후 <N>수정

모든 과정 종료 후 result 문자열 생성
유저 정보 dic도 필요할 듯

"""

def solution(record):
    
    commands = [com.split(" ") for com in record ]
    
    # 유저 정보 저장 딕셔너리
    users = {}
    
    # 명령 저장 리스트
    result = []
    
    for curCom in commands:
        com = curCom[0]
        uid = curCom[1]
        
        if com == "Enter":
            result.append([uid, 0])
            name = curCom[2]
            users[uid] = name
            
        elif com == "Leave":
            result.append([uid,1])
            
        elif com == "Change":
            name = curCom[2]
            users[uid] = name
    """
    print(result)
    print(users)
    
    [['uid1234', 0], ['uid4567', 0], ['uid1234', 1], ['uid1234', 0]]
    {'uid1234': 'Prodo', 'uid4567': 'Ryan'}
    """
    
    answer = []
    
    
    for uid, enter in result:
        name = users[uid]
        
        # 입장시
        if enter == 0:
            curStr = name + "님이 들어왔습니다."
        else:
            curStr = name + "님이 나갔습니다."
            
        answer.append(curStr)
    return answer