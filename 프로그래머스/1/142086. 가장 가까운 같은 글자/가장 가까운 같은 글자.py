def solution(s):
    """
    딕셔너리를 이용하여 필요한 문자만 이용하여 출력값을 계산
    처음 들어온 문자는 -1을 append후, 문자열의 몇번째 요소인지 기록
    2번 이상 들어온 문자는 이전에 기록된 데이터를 바탕으로 다시 연산 후 append
    """
    # 딕셔너리 선언
    count = dict()
    
    #result 리턴용 리스트 생성
    answer = []
    
    # 입력 문자열을 한 글자씩 리스트로 생성
    inputString = list(s)
    
    
    # 입력 문자열이 한 글자씩 저장된 리스트를 0번쨰 요소부터 마지막 요소까지 하나씩 검사
    for i in range(len(inputString)):
        
        #문자가 count라는 딕셔너리에 존재할 경우(이전에 한번 나왔을 경우))
        if inputString[i] in count:
            
            # 거리의 차이를 계산하여 결과값 리스트에 저장
            answer.append(i - count[inputString[i]])
            
        # 문자가 처음 등장했을 경우    
        else:
            
            # -1을 결과값 리스트에 저장
            answer.append(-1)
            
        # 등장한 문자의 위치를 dict에 저장(추후 거리 계산을 위해 사용)
        count[inputString[i]] = i
        
    return answer