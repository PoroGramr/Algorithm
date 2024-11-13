T = int(input())

for t in range(1, T + 1):
    N = int(input())

    data = list(map(int, input().split()))
    # 수업 듣기 시작하는 요일 저장용 변수
    daysClass = []
    for i in range(len(data)):
        if data[i] == 1:
            daysClass.append(i)
    minDays = float("inf")
    for day in daysClass:
        # 수강한 수업 수 카운트
        count = 0

        # 삼성대학교에서 지내야하는 일 수 카운트
        days = 0
        while count != N:

            # 지내야 하는 일수 +1
            days += 1

            # 월화수목금토일 요일 반복
            if day >= 7:
                day %= 7

            # 수업이 있는 요일이라면 수강한 수업 수 +1
            if data[day] == 1:
                count += 1

            # 다음 요일로
            day += 1
        minDays = min(minDays, days)

    print(f"#{t} {minDays}")







