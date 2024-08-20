"""
문제 이해
- 모든 달이 28일 까지 있음
- 입력 
    - today : 오늘의 날짜(문자열)
    - terms : 약관타입과 약관별 정보 저장 가능 유효 기간(리스트/문자열("약관타입 기간"))
    - privacies : 개인정보 저장 시작 날짜와 약관분류(리스트 / 문자열 ("날짜 약관타입"))

- 출력
    - 폐기해야하는 약관의 번호[리스트]
    
    - 약관 번호가 1부터 시작하므로 +1 해야함
아이디어
- 약관 종류랑 유효기간을 저장할 수 있는 공간 {termsTable}(type: month)
- 개인정보 수집일자 + 유효기간 < 오늘 : 파기
- 출력하기
** 연월일 -> 일
    - 1년-> 12개월 * 28일
    - 1개월 : 28일

제한 사항
- terms : 20 n
- privacies : 100 m
"""

def solution(today, terms, privacies):
    # termsTable 만들기 (type : month)
    termsTable = {}
    for t in terms:
        t = t.split()
        termsTable[t[0]] = int(t[1])
    
     # 오늘 날짜를 days로 바꾸기
    todayYear, todayMonth, todayDay = map(int, today.split("."))
    today2days = todayYear * 12 * 28 + todayMonth * 28 + todayDay
    
    print(termsTable)
    answer = []
        
    # privacies를 반복하기
    for idx, prv in enumerate(privacies):
        date, termType = prv.split()
        dateYear, dateMonth, dateDay = map(int, date.split("."))
        date2days = dateYear * 12 * 28 + dateMonth * 28 + dateDay + termsTable[termType] * 28
        
        if date2days <= today2days:
            answer.append(idx + 1)
        
    
    # - 개인정보 수집일자 + 유효기간을 오늘 날짜와 비교
    #   - 오늘보다 이전이면 파기가 필요한 것으로 확인 idx +1
    

    return answer