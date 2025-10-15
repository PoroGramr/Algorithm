"""
메시지를 압축하여 전송 효율을 높이는 작업을 하고자 함
압축 전의 정보를 완벽하게 복원 가능한 무손실 압축 알고리즘을 구현하기로 함 -> LZW

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w + c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다

"""

def solution(msg):
    
    lzwDict = {}
    
    for i in range(65, 91):
        alpabet = chr(i)
        lzwDict[alpabet] = i - 64
    
    maxLen = 1
    maxDictIndex = 26
    
    msgIndex = 0
    
    answer = []
    
    
    while msgIndex < len(msg):
    # 남은 길이와 maxLen 중 작은 값부터 내려가며 탐색
        limit = min(maxLen, len(msg) - msgIndex)
        for j in range(limit, 0, -1):
            w = msg[msgIndex: msgIndex + j]
            if w in lzwDict:
                answer.append(lzwDict[w])      # 2-1) 색인 출력

                next_pos = msgIndex + j        # w 다음 글자 위치 (중요!)
                # 2-2) 사전 추가: w 다음 글자가 존재할 때만
                if next_pos < len(msg):
                    c = msg[next_pos]
                    new_entry = w + c
                    if new_entry not in lzwDict:
                        maxDictIndex += 1
                        lzwDict[new_entry] = maxDictIndex
                        # 최대 탐색 길이 상향(보수적으로)
                        if len(new_entry) > maxLen:
                            maxLen = len(new_entry)

                # 입력 포인터는 w 길이만큼 전진 (중요!)
                msgIndex = next_pos
                break
        # for가 반드시 매치 하나에서 break되므로 while은 진행됨
    
    return answer