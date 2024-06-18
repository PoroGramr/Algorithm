def solution(s):
    """
    입력으로 들어온 문자열을 하나하나 검색하면서 결과값 리스트에 저장하는 방식으로 구현할 예정
    알파벳별로 리스트를 만들어 구현
    처음 들어온 문자는 -1을 append후, 문자열의 몇번째 요소인지 기록
    2번 이상 들어온 문자는 이전에 기록된 데이터를 바탕으로 다시 연산 후 append
    """
    #알파벳 별 넘버링을 하기 위해 만든 리스트
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # 각 알파벳별 카운트를 위해 만든 리스트
    alphabetCount=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
    #result 리턴용 리스트 생성
    answer = []
    
    # 입력 문자열을 한 글자씩 리스트로 생성
    inputString = list(s)
    
    print(inputString)
    
    # 입력 문자열이 한 글자씩 저장된 리스트를 0번쨰 요소부터 마지막 요소까지 하나씩 검사
    for i in range(len(inputString)):
        for a in range(0,26): # 모든 알파벳 검사를 위한 for문
            # 처음들어온 문자를 분류하는 for문
            if inputString[i] == alphabet[a] and alphabetCount[a] == -1:
                # answer에 -1을 append한다.
                answer.append(alphabetCount[a])
                # 현재 문자의 위치값을 업데이트
                alphabetCount[a] = i
                continue
                ## 두번 이상 만나는 문자를 분류하는 for문
            elif inputString[i] == alphabet[a] and alphabetCount[
                a] != -1:
                # 같은 문자가 앞에서 얼마나 가까이에 위치했는지 계산
                nearAlphabetCount = i - alphabetCount[a]
                # answer에 nearAlphabetCount append
                answer.append(nearAlphabetCount)
                # 현재 문자의 위치값을 업데이트
                alphabetCount[a] = i
                continue
    return answer