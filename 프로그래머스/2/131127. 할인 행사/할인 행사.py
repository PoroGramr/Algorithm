from collections import Counter

def solution(want, number, discount):
    # 원하는 제품과 개수를 딕셔너리로 생성
    target = dict(zip(want, number))
    target_count = Counter(target)  # 비교를 위해 Counter 사용
    
    # 10일 연속으로 살펴볼 윈도우 슬라이싱
    answer = 0
    for i in range(len(discount) - 9):
        # 현재 10일 간의 할인 품목 확인
        current_window = Counter(discount[i:i+10])
        # 조건 만족 여부 확인
        if all(current_window[item] >= target[item] for item in target):
            answer += 1
    
    return answer
